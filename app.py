import streamlit as st
import pandas as pd
from src.model import detect_anomalies
from src.visualization import visualize_anomalies

st.set_page_config(page_title="Anomaly Detection Visualizer", layout="wide")
st.title("Anomaly Detection Visualizer")

uploaded = st.file_uploader("📤 Upload a CSV file", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)
    st.write("### Data Preview", df.head())

    num_cols = df.select_dtypes(include=['float64','int64']).columns.tolist()
    x = st.selectbox("X-axis", num_cols)
    y = st.selectbox("Y-axis", num_cols)
    contamination = st.slider("Contamination (fraction of anomalies)", 0.01, 0.5, 0.05)

    df_out = detect_anomalies(df, contamination)
    fig = visualize_anomalies(df_out, x, y)
    st.plotly_chart(fig, use_container_width=True)

    csv = df_out.to_csv(index=False).encode('utf-8')
    st.download_button("Download Results", csv, "anomaly_results.csv", "text/csv")
else:
    st.info("Upload a CSV file to start anomaly detection.")

