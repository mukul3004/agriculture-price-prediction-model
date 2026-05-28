from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import joblib
import os

app = Flask(__name__)

# ── LSTM Model Definition ─────────────────────────────────────────────────────

class LSTMModel(nn.Module):
    def __init__(self):
        super(LSTMModel, self).__init__()
        self.lstm = nn.LSTM(input_size=1, hidden_size=32, batch_first=True)
        self.fc = nn.Linear(32, 1)

    def forward(self, x):
        out, _ = self.lstm(x)
        out = self.fc(out[:, -1, :])
        return out

# ── File Maps ─────────────────────────────────────────────────────────────────

COMMODITY_FILES = {
    "onion":       "data/Onion.csv",
    "rice":        "data/Rice.csv",
    "wheat":       "data/Wheat.csv",
    "cabbage":     "data/Cabbage.csv",
    "cauliflower": "data/Cauliflower.csv",
    "brinjal":     "data/Brinjal.csv",
}

# ── Home Route ────────────────────────────────────────────────────────────────

@app.route('/')
def home():
    return render_template("index.html")

# ── Predict Route ─────────────────────────────────────────────────────────────

@app.route('/predict', methods=['POST'])
def predict():
    commodity = request.form['commodity'].lower().strip()
    days = int(request.form['days'])

    # ── Validate inputs ───────────────────────────────────────────────────────
    if commodity not in COMMODITY_FILES:
        return render_template("index.html", error=f"Unknown commodity: {commodity}")

    if days < 1 or days > 100:
        return render_template("index.html", error="Days must be between 1 and 100.")

    # ── Resolve paths (relative to app.py location) ───────────────────────────
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path  = os.path.join(base_dir, "models", f"{commodity}_lstm_model.pth")
    scaler_path = os.path.join(base_dir, "models", f"{commodity}_scaler.save")
    csv_path    = os.path.join(base_dir, COMMODITY_FILES[commodity])

    # ── Load model ────────────────────────────────────────────────────────────
    model = LSTMModel()
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model.eval()

    # ── Load scaler ───────────────────────────────────────────────────────────
    scaler = joblib.load(scaler_path)

    # ── Load & clean CSV ──────────────────────────────────────────────────────
    df = pd.read_csv(csv_path, skiprows=1)
    df['Price Date'] = pd.to_datetime(df['Price Date'], dayfirst=True)
    df = df.sort_values('Price Date')

    price_series = df['Modal Price'].astype(str).str.replace(',', '').pipe(pd.to_numeric, errors='coerce').dropna().values

    if len(price_series) < 3:
        return render_template("index.html", error="Not enough price data to make a prediction.")

    # ── Prepare seed sequence (last 3 known prices) ───────────────────────────
    last_values   = price_series[-3:]
    scaled_values = scaler.transform(last_values.reshape(-1, 1))
    sequence      = scaled_values.reshape(1, 3, 1)          # (batch, timesteps, features)

    # ── Iterative multi-step forecast ─────────────────────────────────────────
    with torch.no_grad():                                    # FIX: no_grad for inference
        for _ in range(days):
            input_tensor = torch.tensor(sequence, dtype=torch.float32)   # FIX: set dtype directly
            prediction   = model(input_tensor).numpy()                   # no .detach() needed inside no_grad
            sequence     = np.concatenate(
                [sequence[:, 1:, :], prediction.reshape(1, 1, 1)],
                axis=1
            )

    # ── Inverse-transform final prediction ───────────────────────────────────
    predicted_price = scaler.inverse_transform(prediction)   # FIX: use last prediction, not outer var
    wholesale_price = round(float(predicted_price[0][0]), 2)

    # ── Retail estimate: wholesale (₹/quintal) → retail (₹/kg) ───────────────
    # 1 quintal = 100 kg; retail markup is typically 20–30% above wholesale
    retail_price = round((wholesale_price / 100) * 1.25, 2)  # FIX: added 25% retail margin

    return render_template(
        "index.html",
        prediction=wholesale_price,
        retail_price=retail_price,
        commodity=commodity.capitalize(),
        days=days
    )

# ── Run ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app.run(debug=True)