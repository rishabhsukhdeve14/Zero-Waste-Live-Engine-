import streamlit as st
import pandas as pd

st.set_page_config(page_title="Waste.Ai", layout="wide")

st.title("🚀 Waste.Ai")
st.subheader("♻️ Multi-Satellite Live Monitoring Engine")

# CSV LOAD
df = pd.read_csv("live_methane_data.csv", header=None)

# COLUMN NAMES
df.columns = [
    "Timestamp",
    "Landfill_ID",
    "State",
    "City",
    "Latitude",
    "Longitude",
    "Methane",
    "Satellite"
]

# CLEAN DATA
df["Methane"] = pd.to_numeric(df["Methane"], errors="coerce")
df = df.dropna(subset=["Methane"])

# LIVE TABLE
st.subheader("📡 Live Satellite Feed")
st.dataframe(df)

# STATS
st.subheader("📊 Monitoring Stats")

col1, col2 = st.columns(2)

col1.metric("Total Sites", len(df))
col2.metric("Highest Methane", int(df["Methane"].max()))

# TOP ALERT
st.subheader("🚨 High Methane Alerts")

top_sites = df.sort_values(by="Methane", ascending=False).head(5)

st.dataframe(top_sites)