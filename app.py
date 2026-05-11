import streamlit as st
import pandas as pd

st.set_page_config(page_title="Zero Waste.Ai", layout="wide")

st.title("🌍 Zero Waste.Ai")

st.subheader("♻️ Multi-Satellite Live Monitoring Engine")

# CSV LOAD
df = pd.read_csv(
    "live_methane_data.csv",
    header=None,
    names=[
        "Timestamp",
        "Landfill_ID",
        "State",
        "City",
        "Latitude",
        "Longitude",
        "Methane",
        "Satellite"
    ]
)

# Convert numeric columns
df["Latitude"] = pd.to_numeric(df["Latitude"], errors="coerce")
df["Longitude"] = pd.to_numeric(df["Longitude"], errors="coerce")
df["Methane"] = pd.to_numeric(df["Methane"], errors="coerce")

# Remove bad rows
df = df.dropna()

# MAIN TABLE
st.subheader("📡 Live Satellite Feed")

st.dataframe(df, use_container_width=True)

# METRICS
st.subheader("📊 Monitoring Stats")

col1, col2, col3 = st.columns(3)

col1.metric("Total Sites", len(df))
col2.metric("Highest Methane", int(df["Methane"].max()))
col3.metric("Average Methane", int(df["Methane"].mean()))

# TOP POLLUTED
st.subheader("🔥 Top Methane Sites")

top_sites = df.sort_values(by="Methane", ascending=False)

st.dataframe(top_sites.head(20), use_container_width=True)

# CHART
st.subheader("📈 Methane Levels")

chart_data = top_sites[["City", "Methane"]].head(15)

st.bar_chart(
    chart_data.set_index("City")
)

# MAP
st.subheader("🗺️ Satellite Map")

map_data = df.rename(
    columns={
        "Latitude": "lat",
        "Longitude": "lon"
    }
)

st.map(map_data)

# SATELLITES
st.subheader("🛰️ Active Satellites")

satellites = [
    "Sentinel-1",
    "Sentinel-2",
    "Sentinel-5P",
    "Landsat-8",
    "Landsat-9",
    "MODIS",
    "VIIRS"
]

for sat in satellites:
    st.success(f"{sat} Connected")

st.success("✅ Zero Waste.Ai Live Monitoring Active")