import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import IsolationForest

import ee

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="ZeroWaste.AI",
    layout="wide"
)

# ---------------- EARTH ENGINE ----------------

try:
    ee.Initialize(project='stalwart-fx-490910-e3')
    satellite_connected = True

except Exception as e:
    satellite_connected = False
    satellite_error = str(e)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.main {
    background-color: #0e1117;
    color: white;
}

.big-title {
    font-size: 55px;
    font-weight: bold;
    color: #00ffcc;
}

.section-title {
    font-size: 32px;
    font-weight: bold;
    color: white;
}

.metric-box {
    background-color: #161b22;
    padding: 15px;
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.markdown(
    '<p class="big-title">ZeroWaste.AI</p>',
    unsafe_allow_html=True
)

st.markdown("""
# Multi-Satellite Intelligence Dashboard

AI + ESG + Methane Intelligence + Smart Waste Detection
""")

# ---------------- SATELLITE STATUS ----------------

st.markdown("## Satellite Engine")

if satellite_connected:
    st.success("Google Earth Engine Connected")

else:
    st.error("Satellite Engine Not Connected")

# ---------------- DEMO DATA ----------------

cities = [
    "Delhi",
    "Mumbai",
    "Hyderabad",
    "Chennai",
    "Bangalore",
    "Kolkata",
    "Pune",
    "Ahmedabad"
]

methane = np.random.randint(1800, 2300, len(cities))

latitudes = np.random.uniform(8, 35, len(cities))
longitudes = np.random.uniform(68, 97, len(cities))

df = pd.DataFrame({
    "City": cities,
    "Methane": methane,
    "lat": latitudes,
    "lon": longitudes
})

# ---------------- ESG SCORE ----------------

df["ESG Score"] = np.random.uniform(
    40,
    95,
    len(df)
).round(1)

# ---------------- ALERTS ----------------

df["Alert"] = df["Methane"].apply(
    lambda x:
    "Critical" if x > 2200 else "Normal"
)

# ---------------- AI PREDICTION ----------------

df["Index"] = np.arange(len(df))

X = df[["Index"]]
y = df["Methane"]

model = LinearRegression()

model.fit(X, y)

future = np.array([[len(df) + 1]])

prediction = model.predict(future)

predicted_value = max(
    min(
        round(float(prediction[0]), 2),
        2500
    ),
    1700
)

# ---------------- ISOLATION FOREST ----------------

iso_model = IsolationForest(
    contamination=0.2,
    random_state=42
)

df["Anomaly"] = iso_model.fit_predict(
    df[["Methane"]]
)

df["Anomaly"] = df["Anomaly"].map({
    1: "Normal",
    -1: "Anomaly"
})

# ---------------- METRICS ----------------

st.markdown("## Global Intelligence Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Cities Scanned",
    len(df)
)

col2.metric(
    "Average Methane",
    round(df["Methane"].mean(), 2)
)

col3.metric(
    "Critical Zones",
    len(df[df["Methane"] > 2200])
)

col4.metric(
    "Predicted Next 24h",
    predicted_value
)

# ---------------- LIVE DATA ----------------

st.markdown("## Live Intelligence Feed")

st.dataframe(df)

# ---------------- AI PREDICTION ----------------

st.markdown("## AI Methane Prediction")

st.metric(
    "Predicted Methane Next 24h",
    predicted_value
)

# ---------------- LINE CHART ----------------

st.markdown("## Methane Trend")

st.line_chart(df["Methane"])

# ---------------- ANOMALY DETECTION ----------------

st.markdown("## AI Anomaly Detection")

anomalies = df[df["Anomaly"] == "Anomaly"]

if len(anomalies) > 0:

    st.warning("AI Detected Environmental Anomalies")

    st.dataframe(anomalies)

else:

    st.success("No anomalies detected")

# ---------------- HEATMAP ----------------

st.markdown("## Satellite Heatmap")

fig = px.density_mapbox(
    df,
    lat='lat',
    lon='lon',
    z='Methane',
    radius=25,
    center=dict(lat=20.59, lon=78.96),
    zoom=3,
    mapbox_style="open-street-map"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------- LIVE MAP ----------------

st.markdown("## Live Waste Intelligence Map")

st.map(df[["lat", "lon"]])

# ---------------- PIE CHART ----------------

st.markdown("## Risk Distribution")

risk_counts = df["Alert"].value_counts()

pie = go.Figure(
    data=[
        go.Pie(
            labels=risk_counts.index,
            values=risk_counts.values
        )
    ]
)

st.plotly_chart(
    pie,
    use_container_width=True
)

# ---------------- TOP DANGEROUS ----------------

st.markdown("## Top Critical Zones")

danger = df.sort_values(
    by="Methane",
    ascending=False
)

st.dataframe(danger.head(5))

# ---------------- DOWNLOAD ----------------

csv = df.to_csv(index=False).encode('utf-8')

st.download_button(
    "Download Intelligence Report",
    csv,
    "ZeroWaste_AI_Report.csv",
    "text/csv"
)

# ---------------- AI INSIGHTS ----------------

st.markdown("## AI Intelligence Insights")

highest_city = df.loc[
    df["Methane"].idxmax()
]

st.warning(
    f"""
Highest methane concentration detected in {highest_city['City']}

Methane Level: {highest_city['Methane']}

AI Recommendation:
Immediate satellite inspection recommended.
"""
)

# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown("""
### ZeroWaste.AI Intelligence Core

Future Features:
- Real satellite methane
- Drone intelligence
- Carbon prediction AI
- Illegal landfill detection
- Government intelligence system
- Climate anomaly engine
- Smart city environmental scoring
""")