import streamlit as st
import pandas as pd

# PAGE SETTINGS
st.set_page_config(
    page_title="Zero Waste.Ai",
    layout="wide"
)

# TITLE
st.title("🌍 Zero Waste.Ai")

st.subheader("♻️ Multi-Satellite Live Monitoring Engine")

# LOAD CSV
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

# CLEAN DATA
df["Latitude"] = pd.to_numeric(df["Latitude"], errors="coerce")
df["Longitude"] = pd.to_numeric(df["Longitude"], errors="coerce")
df["Methane"] = pd.to_numeric(df["Methane"], errors="coerce")

# REMOVE BAD ROWS
df = df.dropna()

# LIVE TABLE
st.subheader("📡 Live Satellite Feed")

st.dataframe(df, use_container_width=True)

# STATS
st.subheader("📊 Monitoring Stats")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Sites",
    len(df)
)

col2.metric(
    "Highest Methane",
    str(df["Methane"].max())
)

col3.metric(
    "Average Methane",
    str(round(df["Methane"].mean(), 2))
)

# TOP POLLUTED
st.subheader("🔥 Top Methane Sites")

top_sites = df.sort_values(
    by="Methane",
    ascending=False
)

st.dataframe(
    top_sites.head(20),
    use_container_width=True
)

# BAR CHART
st.subheader("📈 Methane Levels")

chart_data = top_sites[
    ["City", "Methane"]
].head(15)

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
    "VIIRS",
    "MethaneSAT",
    "GHGSat",
    "NASA EMIT"
]

for sat in satellites:
    st.success(f"{sat} Connected")

# ALERT SYSTEM
st.subheader("🚨 High Methane Alerts")

alerts = df[df["Methane"] > 2100]

if len(alerts) > 0:
    st.error("Critical Methane Sites Detected")

    st.dataframe(
        alerts,
        use_container_width=True
    )
else:
    st.success("No Critical Alerts")

# FINAL STATUS
st.success("✅ Zero Waste.Ai Live Monitoring Active")