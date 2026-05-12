import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster
import tempfile
import os

st.set_page_config(
    page_title="Waste.Ai",
    page_icon="🚀",
    layout="wide"
)

# =========================
# HEADER
# =========================

st.title("🚀 Waste.Ai")
st.subheader("♻️ Multi-Satellite Live Monitoring Engine")

# =========================
# FILE UPLOAD
# =========================

st.markdown("## 📂 Upload Intelligence File")

uploaded_file = st.file_uploader(
    "Upload CSV / TXT / XLSX",
    type=["csv", "txt", "xlsx"]
)

df = None

# =========================
# READ FILE
# =========================

if uploaded_file is not None:

    st.success(f"✅ File Uploaded: {uploaded_file.name}")

    try:

        # CSV
        if uploaded_file.name.endswith(".csv"):

            try:
                df = pd.read_csv(uploaded_file)

            except:
                uploaded_file.seek(0)

                try:
                    df = pd.read_csv(
                        uploaded_file,
                        encoding="latin1"
                    )

                except:
                    uploaded_file.seek(0)

                    df = pd.read_csv(
                        uploaded_file,
                        sep=None,
                        engine="python"
                    )

        # TXT
        elif uploaded_file.name.endswith(".txt"):

            df