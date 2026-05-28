# AgriPredict AI 🌾

AgriPredict AI is a deep learning–based agricultural commodity price forecasting system developed using Flask and PyTorch. The project predicts future wholesale and retail prices of agricultural commodities using historical market data and LSTM (Long Short-Term Memory) neural networks.

---

## 🚀 Features

* AI-powered commodity price forecasting
* Deep learning using LSTM networks
* Wholesale and retail price estimation
* Interactive modern UI
* Real-time prediction generation
* Multi-commodity support
* Forecast accuracy guidance system
* Responsive frontend design

---

## 📊 Supported Commodities

* Onion
* Rice
* Wheat
* Brinjal
* Cabbage
* Cauliflower

---

## 🧠 Technologies Used

### Backend

* Python
* Flask
* PyTorch
* Pandas
* NumPy
* Scikit-learn

### Frontend

* HTML5
* CSS3
* JavaScript

### Machine Learning

* LSTM Neural Networks
* Time Series Forecasting
* MinMaxScaler
* Sequence Prediction

---

## 📁 Project Structure

```bash
CommodityPricePrediction/
│
├── app/
│   ├── static/
│   │   ├── style.css
│   │   └── script.js
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   ├── models/
│   │   ├── onion_lstm_model.pth
│   │   ├── rice_lstm_model.pth
│   │   └── ...
│   │
│   ├── data/
│   │   ├── Onion.csv
│   │   ├── Rice.csv
│   │   └── ...
│   │
│   └── app.py
│
├── notebooks/
├── README.md
└── requirements.txt
```

---

## ⚙️ How It Works

1. Historical commodity price data is collected.
2. Data is cleaned and normalized.
3. Sequential datasets are generated.
4. LSTM models are trained on time-series data.
5. Flask serves the trained model predictions through a web interface.
6. The application predicts future wholesale and retail prices.

---

## 📈 Forecast Accuracy

| Forecast Range | Accuracy Level  |
| -------------- | --------------- |
| 1 – 15 Days    | High Accuracy   |
| 15 – 30 Days   | Medium Accuracy |
| 30 – 100 Days  | Lower Accuracy  |

---

## ▶️ Run the Project

### Clone Repository

```bash
git clone https://github.com/your-username/CommodityPricePrediction.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Flask App

```bash
python app.py
```

---

## 🌐 Application Preview

* Interactive commodity selection
* AI-powered price forecasting
* Wholesale & retail estimation
* Dynamic accuracy visualization
* Modern responsive UI

---

## 📌 Future Improvements

* Weather-based forecasting
* Real-time API integration
* Advanced transformer models
* Market-wise predictions
* Deployment on cloud platforms

---

## 👨‍💻 Author

**Mukul Bhamgare**

AI & Machine Learning Project using Flask + PyTorch LSTM.
