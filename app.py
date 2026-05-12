import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="ZeroWaste.Ai",
    layout="wide"
)

# =========================
# HEADER
# =========================

st.markdown("""
# 🌎 ZERO WASTE GLOBAL COMMAND CENTER

### AI-Powered Climate Intelligence Platform
""")

st.title("🚀 ZeroWaste.Ai")

st.subheader("♻️ Multi-Satellite Live Monitoring Engine")

# =========================
# LIVE SATELLITE DATA ENGINE
# =========================

cities = [
    "Mumbai",
    "Delhi",
    "Kolkata",
    "Hyderabad",
    "Chennai"
]

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

# =========================
# DATAFRAME
# =========================

df = pd.DataFrame(data)

# =========================
# ALERT ENGINE
# =========================

def get_alert(methane):

    if methane > 2200:
        return "🔴 Critical"

    elif methane > 2000:
        return "🟠 High"

    else:
        return "🟢 Safe"

df["Threat"] = df["Methane"].apply(get_alert)

# =========================
# LIVE TABLE
# =========================

st.subheader("📡 Live Landfill Intelligence Feed")

st.dataframe(
    df[[
        "Timestamp",
        "City",
        "Methane",
        "Threat"
    ]]
)

# =========================
# MONITORING STATS
# =========================

st.subheader("📊 Monitoring Stats")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Sites",
        len(df)
    )

with col2:
    st.metric(
        "Highest Methane",
        int(df["Methane"].max())
    )

with col3:
    critical_count = len(
        df[df["Threat"] == "🔴 Critical"]
    )

    st.metric(
        "Critical Alerts",
        critical_count
    )

# =========================
# TOP ALERTS
# =========================

st.subheader("🚨 Top Methane Alerts")

top_alerts = df.sort_values(
    by="Methane",
    ascending=False
).head(10)

st.dataframe(top_alerts)

# =========================
# LIVE MAP
# =========================

st.subheader("🗺️ Satellite Methane Heatmap")

fig_map = px.scatter_mapbox(
    df,
    lat="Latitude",
    lon="Longitude",
    size="Methane",
    color="Methane",
    hover_name="City",
    zoom=3,
    height=600
)

fig_map.update_layout(
    mapbox_style="open-street-map"
)
# =========================
# REAL AI PREDICTION ENGINE
# =========================

from sklearn.linear_model import LinearRegression

st.subheader("🤖 Real AI Methane Prediction Engine")

df["TimeIndex"] = range(len(df))

X = df[["TimeIndex"]]

y = df["Methane"]

model = LinearRegression()

model.fit(X, y)

future_time = [[len(df) + 24]]

prediction = model.predict(future_time)

st.metric(
    "Predicted Methane Next 24h",
    round(prediction[0], 2)
)

st.plotly_chart(
    fig_map,
    use_container_width=True
)

# =========================
# TREND ANALYSIS
# =========================

st.subheader("📈 Methane Trend Analysis")

fig = px.line(
    df,
    x="Timestamp",
    y="Methane",
    color="City",
    title="Live Methane Emission Trends"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =========================
# REAL AI PREDICTION ENGINE
# =========================

from sklearn.linear_model import LinearRegression

st.subheader("🤖 Real AI Methane Prediction Engine")

df["TimeIndex"] = range(len(df))

X = df[["TimeIndex"]]

y = df["Methane"]

model = LinearRegression()

model.fit(X, y)

future_time = [[len(df) + 24]]

prediction = model.predict(future_time)

st.metric(
    "Predicted Methane Next 24h",
    round(prediction[0], 2)
)

# =========================
# ESG ENGINE
# =========================

st.subheader("🌍 ESG Risk Intelligence")

df["ESG Score"] = (
    100 - (
        (df["Methane"] - 1800) / 5
    )
)

st.dataframe(
    df[[
        "City",
        "Methane",
        "ESG Score"
    ]].head(10)
)

# =========================
# AI CORE
# =========================

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
- AI climate command system
- Global landfill monitoring
""")

# =========================
# AUTO REFRESH
# =========================

time.sleep(5)

st.rerun()