import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import plotly.express as px
import plotly.graph_objects as go

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="ZeroWaste.AI",
    page_icon="🚀",
    layout="wide"
)

# =========================================
# CUSTOM CSS
# =========================================

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

.metric-box {
    background-color: #161b22;
    padding: 20px;
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# HEADER
# =========================================

st.markdown(
    '<p class="big-title">🚀 ZeroWaste.AI</p>',
    unsafe_allow_html=True
)

st.markdown("""
# ♻️ Multi-Satellite Intelligence Dashboard

AI + ESG + Methane Intelligence + Smart Waste Detection
""")

# =========================================
# AUTO LIVE DATA
# =========================================

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

methane_values = np.random.randint(
    1700,
    2700,
    len(cities)
)

df = pd.DataFrame({
    "City": cities,
    "Methane": methane_values
})

# =========================================
# AUTO LAT LON
# =========================================

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

# =========================================
# ESG SCORE
# =========================================

df["ESG Score"] = np.random.uniform(
    20,
    99,
    len(df)
).round(1)

# =========================================
# ALERT ENGINE
# =========================================

df["Alert"] = df["Methane"].apply(
    lambda x:
    "🔴 Critical"
    if x > 2300
    else (
        "🟠 High"
        if x > 2100
        else "🟢 Safe"
    )
)

# =========================================
# AI PREDICTION
# =========================================

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

# =========================================
# TOP METRICS
# =========================================

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
    "Critical Zones",
    len(df[df["Methane"] > 2300])
)

c4.metric(
    "Predicted Next 24h",
    predicted_value
)

# =========================================
# MAIN DATAFRAME
# =========================================

st.markdown("## 🌍 Live Intelligence Feed")

st.dataframe(
    df,
    use_container_width=True
)

# =========================================
# AI PREDICTION PANEL
# =========================================

st.markdown("## 🤖 AI Methane Prediction")

st.success(
    f"Predicted methane level in next 24h: {predicted_value}"
)

# =========================================
# LINE CHART
# =========================================

st.markdown("## 📈 Methane Trend Analysis")

fig_line = px.line(
    df,
    x="City",
    y="Methane",
    markers=True,
    title="Methane Intelligence Trend"
)

st.plotly_chart(
    fig_line,
    use_container_width=True
)

# =========================================
# HEATMAP
# =========================================

st.markdown("## 🛰️ Satellite Methane Heatmap")

fig_map = px.density_mapbox(
    df,
    lat="lat",
    lon="lon",
    z="Methane",
    radius=30,
    center=dict(
        lat=20.59,
        lon=78.96
    ),
    zoom=3,
    mapbox_style="open-street-map"
)

st.plotly_chart(
    fig_map,
    use_container_width=True
)

# =========================================
# LIVE MAP
# =========================================

st.markdown("## 🌎 Live Waste Intelligence Map")

st.map(
    df[["lat", "lon"]]
)

# =========================================
# ESG TABLE
# =========================================

st.markdown("## 🌱 ESG Intelligence")

st.dataframe(
    df[[
        "City",
        "Methane",
        "ESG Score",
        "Alert"
    ]]
)

# =========================================
# PIE CHART
# =========================================

st.markdown("## ♻️ Risk Distribution")

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

# =========================================
# TOP DANGEROUS CITIES
# =========================================

st.markdown("## ☢️ Top Dangerous Cities")

top_danger = df.sort_values(
    by="Methane",
    ascending=False
)

st.dataframe(
    top_danger.head(10),
    use_container_width=True
)

# =========================================
# DOWNLOAD REPORT
# =========================================

csv = df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    "⬇️ Download Intelligence Report",
    csv,
    "ZeroWaste_AI_Report.csv",
    "text/csv"
)

# =========================================
# AI INSIGHTS
# =========================================

st.markdown("## 🧠 AI Intelligence Insights")

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

# =========================================
# FOOTER
# =========================================

st.markdown("---")

st.markdown("""

## 🚀 ZeroWaste.AI Intelligence Core

Future AI Systems:
- Real satellite integration
- Illegal landfill detection
- Carbon emission AI
- Smart city intelligence
- Climate risk engine
- Government ESG dashboard
- AI anomaly detection
- Global methane monitoring

""")