import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time

st.set_page_config(page_title="ZeroWaste.Ai", layout="wide")

st.title("🚀 ZeroWaste.Ai")

st.subheader("♻️ Multi-Satellite Live Monitoring Engine")

# Fake live satellite intelligence data
cities = ["Mumbai", "Delhi", "Kolkata", "Hyderabad", "Chennai"]

data = []

for i in range(50):
    city = np.random.choice(cities)

    methane = np.random.randint(1800, 2300)

    if city == "Mumbai":
        lat, lon = 19.0760, 72.8777
    elif city == "Delhi":
        lat, lon = 28.6139, 77.2090
    elif city == "Kolkata":
        lat, lon = 22.5726, 88.3639
    elif city == "Hyderabad":
        lat, lon = 17.3850, 78.4867
    else:
        lat, lon = 13.0827, 80.2707

    data.append({
        "Timestamp": pd.Timestamp.now(),
        "City": city,
        "Methane": methane,
        "Latitude": lat,
        "Longitude": lon
    })

df = pd.DataFrame(data)

# LIVE TABLE
st.subheader("📡 Live Landfill Sites")

st.dataframe(df)

# STATS
st.subheader("📊 Monitoring Stats")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Sites", len(df))

with col2:
    st.metric("Highest Methane", int(df["Methane"].max()))

# ALERTS
st.subheader("🚨 Top Methane Alerts")

top_alerts = df.sort_values(by="Methane", ascending=False).head(10)

st.dataframe(top_alerts)

# MAP
st.subheader("🗺️ Live Landfill Map")

map_df = df.rename(columns={
    "Latitude": "lat",
    "Longitude": "lon"
})

st.map(map_df)

# CHART
st.subheader("📈 Methane Trend Analysis")

fig = px.line(
    df,
    x="Timestamp",
    y="Methane",
    color="City",
    title="Live Methane Emission Trends"
)

st.plotly_chart(fig, use_container_width=True)

# AI SECTION
st.markdown("---")

st.markdown("""
## 🧠 ZeroWaste.Ai Intelligence Core

### Future AI Features:
- Methane hotspot prediction
- Illegal landfill detection
- ESG risk scoring
- Satellite anomaly alerts
- Government intelligence dashboard
- Carbon credit intelligence
- AI waste heatmaps
- Climate risk prediction engine
""")