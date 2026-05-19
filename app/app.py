from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import joblib

app = Flask(__name__)

# =========================
# LSTM MODEL
# =========================

class LSTMModel(nn.Module):

    def __init__(self):

        super(LSTMModel, self).__init__()

        self.lstm = nn.LSTM(
            input_size=1,
            hidden_size=50,
            batch_first=True
        )

        self.fc = nn.Linear(
            50,
            1
        )

    def forward(self, x):

        out, _ = self.lstm(x)

        out = self.fc(out[:, -1, :])

        return out


# =========================
# HOME PAGE
# =========================

@app.route('/')
def home():

    return render_template("index.html")


# =========================
# PREDICT ROUTE
# =========================

@app.route('/predict', methods=['POST'])
def predict():

    commodity = request.form['commodity']
    days = int(request.form['days'])

    # =========================
    # LOAD MODEL
    # =========================

    model_path = f"models/{commodity.lower()}_lstm_model.pth"

    model = LSTMModel()

    model.load_state_dict(
        torch.load(
            model_path,
            map_location=torch.device('cpu')
        )
    )

    model.eval()

    # =========================
    # LOAD SCALER
    # =========================

    scaler_path = f"models/{commodity.lower()}_scaler.save"

    scaler = joblib.load(scaler_path)

    # =========================
    # LOAD DATASET
    # =========================

    df = pd.read_csv(
        "data/Price_Agriculture_commodities_Week.csv"
    )

    commodity_df = df[
        df['Commodity'].str.lower() == commodity.lower()
    ]

    commodity_df['Arrival_Date'] = pd.to_datetime(
        commodity_df['Arrival_Date'],
        dayfirst=True
    )

    commodity_df = commodity_df.sort_values(
        'Arrival_Date'
    )

    price_series = commodity_df.groupby(
        'Arrival_Date'
    )['Modal Price'].mean().values

    # =========================
    # LAST 3 VALUES
    # =========================

    last_values = price_series[-3:]

    scaled_values = scaler.transform(
        last_values.reshape(-1, 1)
    )

    sequence = scaled_values.reshape(1, 3, 1)

    # =========================
    # FUTURE PREDICTION
    # =========================

    predicted_price = 0

    for i in range(days):

        input_tensor = torch.tensor(
            sequence.astype(np.float32)
        )

        prediction = model(input_tensor)

        prediction = prediction.detach().numpy()

        sequence = np.concatenate(
    (
        sequence[:, 1:, :],
        prediction.reshape(1, 1, 1)
    ),
    axis=1
)

        predicted_price = prediction

    predicted_price = scaler.inverse_transform(
        predicted_price
    )

    wholesale_price = round(
        float(predicted_price[0][0]),
        2
    )

    retail_price = round(
        wholesale_price / 100,
        2
    )

    return render_template(
        "index.html",
        prediction=wholesale_price,
        retail_price=retail_price,
        commodity=commodity,
        days=days
    )


# =========================
# RUN APP
# =========================

if __name__ == "__main__":

    app.run(debug=True)