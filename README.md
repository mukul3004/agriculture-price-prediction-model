# 🌾 Agriculture Commodity Price Prediction

A Flask + PyTorch based web application that predicts future wholesale prices of agricultural commodities using LSTM (Long Short-Term Memory) deep learning models.

---

## 🚀 Features

- Predict commodity prices using LSTM neural networks
- Supports multiple commodities:
  - Onion
  - Brinjal
  - Rice
  - Wheat
  - Cabbage
  - Cauliflower
- Clean web interface using Flask
- Retail price estimation per kg
- Trained PyTorch models for each commodity

---

## 🛠️ Tech Stack

- Python
- Flask
- PyTorch
- Pandas
- NumPy
- Scikit-learn
- HTML/CSS

---

## 📂 Project Structure

```bash
CommodityPricePrediction/
│
├── app/
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── style.css
│
├── data/
│   └── Price_Agriculture_Commodities_Week.csv
│
├── models/
│   ├── onion_lstm_model.pth
│   ├── onion_scaler.save
│   ├── brinjal_lstm_model.pth
│   ├── brinjal_scaler.save
│   ├── cabbage_lstm_model.pth
│   ├── cabbage_scaler.save
│   ├── cauliflower_lstm_model.pth
│   ├── cauliflower_scaler.save
│   ├── rice_lstm_model.pth
│   ├── rice_scaler.save
│   ├── wheat_lstm_model.pth
│   └── wheat_scaler.save
│
├── notebooks/
│   └── lstm_price_prediction.ipynb
│
├── requirements.txt
└── README.md