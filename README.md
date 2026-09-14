# 🛡️ Network Intrusion Detection System

A Machine Learning-based Network Intrusion Detection System developed using the CICIDS2017 dataset. The application detects malicious network traffic and classifies different types of cyber attacks using a Random Forest classifier.

## 📌 Project Overview

This project analyzes network traffic data and predicts whether the traffic is normal or belongs to a specific attack category.

The model is trained on the CICIDS2017 dataset and deployed through a Streamlit web application.

## 🎯 Features

- Upload network traffic CSV files
- Detect malicious network activity
- Classify multiple attack categories
- Display prediction results instantly
- Visualize attack distribution
- Download prediction results as CSV

## 🧠 Machine Learning Model

Algorithm Used:

- Random Forest Classifier

Preprocessing Steps:

- Label Encoding
- Feature Scaling using StandardScaler
- Train-Test Split
- Model Training and Evaluation

## 📊 Dataset

Dataset Used:

CICIDS2017 Cleaned and Preprocessed Dataset

Contains:

- Normal Traffic
- DoS Attacks
- DDoS Attacks
- Port Scanning
- Brute Force Attacks
- Web Attacks
- Bot Attacks

Dataset Source:

https://www.kaggle.com/datasets/ericanacletoribeiro/cicids2017-cleaned-and-preprocessed

## 🏗️ Project Structure

```text
network-intrusion-detector/
│
├── app.py
├── rf_model_small.pkl
├── scaler.pkl
├── label_encoder.pkl
├── requirements.txt
├── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/network-intrusion-detector.git
cd network-intrusion-detector
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## 🚀 Deployment

The application is deployed using Streamlit Community Cloud.

## 📈 Model Workflow

```text
Network Traffic Data
          ↓
Data Preprocessing
          ↓
Feature Scaling
          ↓
Random Forest Model
          ↓
Attack Prediction
          ↓
Visualization & Results
```

## 📊 Evaluation Metrics

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

## 🔮 Future Improvements

- Real-time packet capture integration
- Deep Learning based intrusion detection
- Live network monitoring dashboard
- Threat severity scoring
- Alert notification system

## 👨‍💻 Author

Devadarshan R R

Engineering Student | Machine Learning | Cybersecurity

## 📜 License

This project is developed for educational and research purposes.
