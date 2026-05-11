import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Waste.Ai", layout="wide")

st.title("🚀 Waste.Ai")
st.subheader("♻️ Multi-Satellite Live Monitoring Engine")

# LOAD CSV
df = pd.read_csv("live_methane_data.csv", header=None)

# AUTO FIX EXTRA COLUMNS
df = df.iloc[:, :8]

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
df["Latitude"] = pd.to_numeric(df["Latitude"], errors="coerce")
df["Longitude"] = pd.to_numeric(df["Longitude"], errors="coerce")

df = df.dropna()

# LIVE TABLE
st.subheader("📡 Live Landfill Sites")
st.dataframe(df)

# STATS
st.subheader("📊 Monitoring Stats")

col1, col2 = st.columns(2)

col1.metric("Total Sites", len(df))
col2.metric("Highest Methane", int(df["Methane"].max()))

# ALERTS
st.subheader("🚨 Top Methane Alerts")

top_sites = df.sort_values(
    by="Methane",
    ascending=False
).head(10)

st.dataframe(top_sites)

# LIVE MAP
st.subheader("🗺️ Live Landfill Map")

# CREATE MAP
m = folium.Map(
    location=[22.5, 80.0],
    zoom_start=5
)

# ADD LANDFILL MARKERS
for _, row in df.iterrows():

    methane = row["Methane"]

    # COLOR CONDITIONS
    if methane > 2100:
        color = "red"

    elif methane > 1950:
        color = "orange"

    else:
        color = "green"

    folium.CircleMarker(
        location=[
            row["Latitude"],
            row["Longitude"]
        ],

        radius=8,

        popup=f"""
        <b>City:</b> {row['City']}<br>
        <b>State:</b> {row['State']}<br>
        <b>Methane:</b> {methane}<br>
        <b>Satellite:</b> {row['Satellite']}
        """,

        color=color,
        fill=True,
        fill_color=color

    ).add_to(m)

# SHOW MAP
st_folium(
    m,
    width=1200,
    height=600
)