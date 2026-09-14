import streamlit as st
import pandas as pd
import joblib

# Load saved files
model = joblib.load("rf_model_small.pkl")
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("label_encoder.pkl")

# Page settings
st.set_page_config(
    page_title="Network Intrusion Detection",
    page_icon="🛡️",
    layout="wide"
)

# Title
st.title("🛡️ Network Intrusion Detection System")
st.write("Upload a CSV file containing network traffic data and detect potential attacks.")

# Upload CSV
uploaded_file = st.file_uploader(
    "Upload Network Traffic CSV",
    type=["csv"]
)

if uploaded_file is not None:

    try:
        # Read CSV
        df = pd.read_csv(uploaded_file)

        st.subheader("Uploaded Dataset")
        st.dataframe(df.head())

        st.write(f"Rows: {df.shape[0]}")
        st.write(f"Columns: {df.shape[1]}")

        # Predict button
        if st.button("Run Detection"):

            # Scale data
            X_scaled = scaler.transform(df)

            # Predict
            predictions = model.predict(X_scaled)

            # Convert numeric labels back to names
            attack_labels = encoder.inverse_transform(predictions)

            # Create result dataframe
            result_df = df.copy()
            result_df["Prediction"] = attack_labels

            st.subheader("Prediction Results")
            st.dataframe(result_df.head(20))

            # Attack summary
            st.subheader("Attack Summary")

            attack_counts = pd.Series(
                attack_labels
            ).value_counts()

            st.bar_chart(attack_counts)

            st.write(attack_counts)

            # Download results
            csv = result_df.to_csv(index=False)

            st.download_button(
                label="Download Results",
                data=csv,
                file_name="intrusion_detection_results.csv",
                mime="text/csv"
            )

    except Exception as e:
        st.error(f"Error: {e}")

else:
    st.info("Please upload a CSV file to begin detection.")
