import streamlit as st
import pandas as pd
import joblib

# Load model files
model = joblib.load("rf_model_small.pkl")
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("label_encoder.pkl")

st.set_page_config(
    page_title="CyberGuard AI",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ CyberGuard AI")
st.caption("Network Intrusion Detection Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

uploaded_file = st.file_uploader(
    "Upload Network Traffic CSV",
    type=["csv"]
)

prompt = st.chat_input("Ask CyberGuard AI to analyze your traffic...")

if prompt:

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    if uploaded_file is None:

        response = """
Please upload a network traffic CSV file first.
"""

        with st.chat_message("assistant"):
            st.markdown(response)

        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )

    else:

        df = pd.read_csv(uploaded_file)

        X_scaled = scaler.transform(df)

        predictions = model.predict(X_scaled)

        labels = encoder.inverse_transform(predictions)

        attack_counts = pd.Series(labels).value_counts()

        total = len(labels)

        summary = []

        for attack, count in attack_counts.items():
            percentage = (count / total) * 100
            summary.append(
                f"- **{attack}** : {count} records ({percentage:.2f}%)"
            )

        response = f"""
### Analysis Complete

Total Records Analyzed: **{total}**

### Detected Traffic Types

{chr(10).join(summary)}

### Security Assessment

The uploaded network traffic has been analyzed successfully.
Review the detected attack categories and investigate any malicious traffic.
"""

        with st.chat_message("assistant"):
            st.markdown(response)

            st.subheader("Traffic Distribution")
            st.bar_chart(attack_counts)

        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )
