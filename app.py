import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import plotly.express as px
import plotly.graph_objects as go

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="ZeroWaste.AI",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

.big-title {
    font-size: 60px;
    font-weight: bold;
    color: #00ffcc;
}

.section-title {
    font-size: 35px;
    font-weight: bold;
    color: white;
}

[data-testid="stMetricValue"] {
    color: #00ff99;
    font-size: 35px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.markdown(
    '<p class="big-title">🚀 ZeroWaste.AI</p>',
    unsafe_allow_html=True
)

st.markdown("""
# ♻️ Multi-Satellite Intelligence Dashboard

AI + ESG + Methane Intelligence + Smart Waste Detection
""")

# ---------------- SAMPLE DATA ----------------

df = pd.DataFrame({
    "City": [
        "Delhi",
        "Mumbai",
        "Hyderabad",
        "Chennai",
        "Kolkata",
        "Bangalore",
        "Pune",
        "Ahmedabad"
    ],

    "Methane": [
        2200,
        1800,
        2500,
        1900,
        2400,
        2000,
        1750,
        2600
    ]
})

# ---------------- LAT LON ----------------

df["lat"] = np.random.uniform(
    8,
    35,
    len(df)
)

df["lon"] = np.random.uniform(
    68,
    97,
    len(df)
)

# ---------------- AI MODEL ----------------

df["Index"] = np.arange(len(df))

X = df[["Index"]]
y = df["Methane"]

model = LinearRegression()
model.fit(X, y)

future = np.array([[len(df) + 24]])

prediction = model.predict(future)

predicted_value = round(
    float(prediction[0]),
    2
)

# ---------------- ESG ----------------

df["ESG Score"] = np.random.uniform(
    10,
    99,
    len(df)
).round(1)

# ---------------- ALERT ----------------

df["Alert"] = df["Methane"].apply(
    lambda x:
    "⚠️ Illegal Waste Zone"
    if x > 2200
    else "✅ Safe"
)

# ---------------- METRICS ----------------

st.markdown("## 📊 Global Intelligence Metrics")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Cities Scanned",
    len(df)
)

c2.metric(
    "Average Methane",
    round(df["Methane"].mean(), 2)
)

c3.metric(
    "High Risk Zones",
    len(df[df["Methane"] > 2200])
)

c4.metric(
    "Predicted Next 24h",
    predicted_value
)

# ---------------- AI PREDICTION ----------------

st.markdown(
    "## 🤖 Real AI Methane Prediction Engine"
)

st.metric(
    "Predicted Methane Next 24h",
    predicted_value
)

# ---------------- LINE CHART ----------------

st.markdown("## 📈 Methane Trend Analysis")

st.line_chart(df["Methane"])

# ---------------- ESG TABLE ----------------

st.markdown("## 🌍 ESG Risk Intelligence")

st.dataframe(df)

# ---------------- ALERT TABLE ----------------

st.markdown("## 🚨 Illegal Waste Detection")

danger = df[df["Methane"] > 2200]

if len(danger) > 0:

    st.error(
        "⚠️ HIGH RISK ZONES DETECTED"
    )

    st.dataframe(danger)

else:

    st.success(
        "✅ No Dangerous Zones"
    )

# ---------------- HEATMAP ----------------

st.markdown(
    "## 🛰️ Satellite Methane Heatmap"
)

fig = px.density_mapbox(
    df,
    lat="lat",
    lon="lon",
    z="Methane",
    radius=25,
    center=dict(
        lat=20.59,
        lon=78.96
    ),
    zoom=3,
    mapbox_style="open-street-map"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------- LIVE MAP ----------------

st.markdown(
    "## 🌎 Live Waste Intelligence Map"
)

st.map(
    df[["lat", "lon"]]
)

# ---------------- PIE CHART ----------------

st.markdown(
    "## ♻️ Risk Distribution"
)

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

# ---------------- TOP CITIES ----------------

st.markdown(
    "## ☢️ Top Dangerous Cities"
)

top_danger = df.sort_values(
    by="Methane",
    ascending=False
).head(10)

st.dataframe(top_danger)

# ---------------- DOWNLOAD REPORT ----------------

csv = df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    "⬇️ Download Intelligence Report",
    csv,
    "ZeroWaste_AI_Report.csv",
    "text/csv"
)

# ---------------- AI INSIGHTS ----------------

st.markdown(
    "## 🧠 AI Intelligence Insights"
)

highest_city = df.loc[
    df["Methane"].idxmax()
]

st.warning(f"""

Highest methane detected in:
{highest_city['City']}

Methane Level:
{highest_city['Methane']}

AI Recommendation:
Immediate satellite inspection recommended.

""")

# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown("""

## 🚀 ZeroWaste.AI Intelligence Core

Future AI Features:

- Methane hotspot prediction
- Illegal landfill detection
- ESG risk scoring
- Satellite anomaly alerts
- Government intelligence dashboard
- Carbon emission AI
- Smart city intelligence

""")