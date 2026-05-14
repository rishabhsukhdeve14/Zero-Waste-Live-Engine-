import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="ZERO WASTE AI",
    layout="wide"
)

# SIDEBAR
st.sidebar.title("ZERO WASTE AI")

city = st.sidebar.selectbox(
    "Monitor City",
    ["Delhi", "Mumbai", "Chennai", "Bangalore"]
)

sensitivity = st.sidebar.slider(
    "AI Scan Sensitivity",
    0,
    100,
    90
)

mode = st.sidebar.selectbox(
    "Detection Mode",
    ["Waste Monitoring", "Methane Scan", "Risk Intelligence"]
)

# HEADER
st.title("🌍 ZERO WASTE AI")
st.success("Environmental Intelligence System Active")

# METRICS
col1, col2, col3 = st.columns(3)

col1.metric("Cities Scanned", "24", "+3")
col2.metric("Methane Flux", "1922.53", "+12%")
col3.metric("AI Accuracy", "96%", "+1.2%")

st.divider()

# UPLOAD
st.subheader("📂 Upload Intelligence File")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("Dataset Uploaded Successfully")

    st.subheader("📄 Live Intelligence Table")

    st.dataframe(df.head(50), use_container_width=True)

    st.subheader("🧠 Dataset Information")

    st.write("Rows:", df.shape[0])
    st.write("Columns:", df.shape[1])

    st.subheader("📋 Columns")

    st.json(list(df.columns))