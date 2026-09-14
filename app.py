import streamlit as st
import pandas as pd
import joblib

model = joblib.load("rf_model.pkl")
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("label_encoder.pkl")

st.title("Network Intrusion Detection System")

uploaded_file = st.file_uploader(
    "Upload Network Traffic CSV",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Data")
    st.dataframe(df.head())

    X = scaler.transform(df)

    predictions = model.predict(X)

    labels = encoder.inverse_transform(predictions)

    result = pd.DataFrame({
        "Prediction": labels
    })

    st.subheader("Predictions")
    st.dataframe(result)

    st.bar_chart(result["Prediction"].value_counts())
