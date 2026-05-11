import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Zero Waste Live Engine", layout="wide")

st.title("🚀 Zero Waste Live Engine")

st.subheader("♻️ Live Landfill Monitoring")

# Auto refresh
time.sleep(1)

# CSV Load
df = pd.read_csv(
    "live_methane_data.csv",
    header=None,
    names=[
        "Timestamp",
        "Landfill ID",
        "State",
        "City",
        "Latitude",
        "Longitude",
        "Methane",
        "Source"
    ]
)

# Main Table
st.dataframe(df, use_container_width=True)

# Metrics
st.subheader("📊 Monitoring Stats")

col1, col2, col3 = st.columns(3)

col1.metric("Total Sites", len(df))
col2.metric("Highest Methane", int(df["Methane"].max()))
col3.metric("Average Methane", int(df["Methane"].mean()))

# Top Polluted Sites
st.subheader("🔥 Top Polluted Landfills")

top_sites = df.sort_values(by="Methane", ascending=False)

st.dataframe(top_sites.head(10), use_container_width=True)

# Chart
st.subheader("📈 Methane Levels")

chart_data = df[["City", "Methane"]]

st.bar_chart(
    chart_data.set_index("City")
)

# Map
st.subheader("🗺️ Landfill Map")

map_data = df.rename(
    columns={
        "Latitude": "lat",
        "Longitude": "lon"
    }
)

st.map(map_data)

st.success("✅ Live Monitoring Active")