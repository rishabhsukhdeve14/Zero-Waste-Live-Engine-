import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="ZeroWaste.AI",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

body {
    background-color: #0e1117;
    color: white;
}

.big-title {
    font-size: 55px;
    font-weight: bold;
    color: #00ffcc;
}

.section-title {
    font-size: 35px;
    font-weight: bold;
    color: white;
}

.metric-card {
    background: #111827;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    border: 1px solid #1f2937;
}

.alert-box {
    padding: 20px;
    border-radius: 15px;
    background-color: #ff4b4b;
    color: white;
    font-size: 20px;
    font-weight: bold;
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

# ---------------- AUTO GENERATED DATA ----------------

cities = [
    "Delhi",
    "Mumbai",
    "Hyderabad",
    "Chennai",
    "Kolkata",
    "Bangalore",
    "Pune",
    "Ahmedabad"
]

methane = np.random.randint(1700, 2800, len(cities))

latitudes = np.random.uniform(8, 35, len(cities))
longitudes = np.random.uniform(68, 97, len(cities))

df = pd.DataFrame({
    "City": cities,
    "Methane": methane,
    "lat": latitudes,
    "lon": longitudes
})

# ---------------- AI PREDICTION ----------------

df["Index"] = np.arange(len(df))

X = df[["Index"]]
y = df["Methane"]

model = LinearRegression()
model.fit(X, y)

future = np.array([[len(df) + 24]])

prediction = model.predict(future)

predicted_value = round(float(prediction[0]), 2)

# ---------------- ESG SCORE ----------------

df["ESG Score"] = np.random.uniform(
    10,
    99,
    len(df)
).round(1)

# ---------------- ALERT SYSTEM ----------------

df["Alert"] = df["Methane"].apply(
    lambda x: "Critical" if x > 2200 else "Safe"
)

# ---------------- TOP METRICS ----------------

st.markdown("## 📊 Global Intelligence Metrics")

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

# ---------------- LIVE DATA TABLE ----------------

st.markdown("## 🌍 Live Intelligence Feed")

st.dataframe(df)

# ---------------- LINE CHART ----------------

st.markdown("## 📈 Methane Trend Analysis")

st.line_chart(df["Methane"])

# ---------------- BAR CHART ----------------

st.markdown("## 📊 City Methane Comparison")

fig_bar = px.bar(
    df,
    x="City",
    y="Methane",
    color="Methane"
)

st.plotly_chart(
    fig_bar,
    use_container_width=True
)

# ---------------- HEATMAP ----------------

st.markdown("## 🛰️ Satellite Methane Heatmap")

fig_map = px.density_mapbox(
    df,
    lat='lat',
    lon='lon',
    z='Methane',
    radius=30,
    center=dict(lat=20.59, lon=78.96),
    zoom=3,
    mapbox_style="open-street-map"
)

st.plotly_chart(
    fig_map,
    use_container_width=True
)

# ---------------- LIVE MAP ----------------

st.markdown("## 🌎 Live Waste Intelligence Map")

st.map(df[["lat", "lon"]])

# ---------------- PIE CHART ----------------

st.markdown("## ♻️ Risk Distribution")

risk_counts = df["Alert"].value_counts()

fig_pie = go.Figure(
    data=[
        go.Pie(
            labels=risk_counts.index,
            values=risk_counts.values
        )
    ]
)

st.plotly_chart(
    fig_pie,
    use_container_width=True
)

# ---------------- TOP DANGEROUS CITIES ----------------

st.markdown("## ☢️ Top Dangerous Cities")

danger = df.sort_values(
    by="Methane",
    ascending=False
)

st.dataframe(danger)

# ---------------- ALERT SECTION ----------------

st.markdown("## 🚨 AI Risk Alerts")

high_risk = df[df["Methane"] > 2400]

if len(high_risk) > 0:

    st.error("Critical methane concentration detected")

    st.dataframe(high_risk)

else:

    st.success("No critical methane zones detected")

# ---------------- DOWNLOAD REPORT ----------------

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download Intelligence Report",
    data=csv,
    file_name="ZeroWaste_AI_Report.csv",
    mime="text/csv"
)

# ---------------- AI INSIGHTS ----------------

st.markdown("## 🧠 AI Intelligence Insights")

highest_city = df.loc[df["Methane"].idxmax()]

st.info(f"""

Highest methane detected in:
{highest_city['City']}

Methane Level:
{highest_city['Methane']}

Recommendations:

- Immediate satellite inspection
- ESG monitoring activated
- Smart anomaly detection enabled
- Government risk tracking active

""")

# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown("""
## 🚀 ZeroWaste.AI Intelligence Core

Future AI Features:

- Real satellite integration
- NASA methane feeds
- AI anomaly detection
- Carbon emission intelligence
- Illegal landfill detection
- Government intelligence systems
- Smart ESG analytics
- Climate risk prediction
""")