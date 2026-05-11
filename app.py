import streamlit as st
import pandas as pd

st.set_page_config(page_title="Waste.Ai", layout="wide")

st.title("🚀 Waste.Ai")
st.subheader("♻️ Multi-Satellite Live Monitoring Engine")

# LOAD CSV
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

# CLEAN
df["Methane"] = pd.to_numeric(df["Methane"], errors="coerce")
df = df.dropna()

# SHOW DATA
st.subheader("📡 Live Landfill Sites")

st.dataframe(df[[
    "Landfill_ID",
    "State",
    "City",
    "Latitude",
    "Longitude",
    "Methane",
    "Satellite"
]])

# STATS
st.subheader("📊 Monitoring Stats")

col1, col2 = st.columns(2)

col1.metric("Total Sites", len(df))
col2.metric("Highest Methane", int(df["Methane"].max()))

# TOP ALERTS
st.subheader("🚨 Top Methane Alerts")

alerts = df.sort_values(by="Methane", ascending=False).head(10)

st.dataframe(alerts)