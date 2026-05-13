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

html, body, [class*="css"] {
    background-color: #0e1117;
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

.metric-box {
    background-color: #111827;
    padding: 20px;
    border-radius: 20px;
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

# ---------------- SAMPLE DATA ----------------

np.random.seed(42)

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
    1800,
    2800,
    size=len(cities)
)

latitudes = [
    28.6139,
    19.0760,
    17.3850,
    13.0827,
    22.5726,
    12.9716,
    18.5204,
    23.0225
]

longitudes = [
    77.2090,
    72.8777,
    78.4867,
    80.2707,
    88.3639,
    77.5946,
    73.8567,
    72.5714
]

# ---------------- DATAFRAME ----------------

df = pd.DataFrame({
    "City": cities,
    "Methane": methane_values,
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

predicted_value = round(
    float(prediction[0]),
    2
)

# ---------------- ESG SCORE ----------------

df["ESG Score"] = np.random.uniform(
    10,
    99,
    len(df)
).round(1)

# ---------------- RISK ENGINE ----------------

def detect_risk(x):

    if x > 2500:
        return "Critical"

    elif x > 2200:
        return "Warning"

    else:
        return "Safe"

df["Risk"] = df["Methane"].apply(detect_risk)

# ---------------- TOP METRICS ----------------

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
    len(df[df["Methane"] > 2500])
)

col4.metric(
    "Predicted Next 24h",
    predicted_value
)

# ---------------- ALERT ENGINE ----------------

st.markdown("## AI Alert Engine")

if predicted_value > 3000:

    st.error(
        "Critical methane concentration detected"
    )

elif predicted_value > 2400:

    st.warning(
        "Methane concentration increasing"
    )

else:

    st.success(
        "Environment stable"
    )

# ---------------- LIVE DATA ----------------

st.markdown("## Live Intelligence Feed")

st.dataframe(df)

# ---------------- LINE CHART ----------------

st.markdown("## Methane Trend Analysis")

fig_line = px.line(
    df,
    x="City",
    y="Methane",
    markers=True,
    title="Methane Levels Across Cities"
)

st.plotly_chart(
    fig_line,
    use_container_width=True
)

# ---------------- ESG CHART ----------------

st.markdown("## ESG Risk Intelligence")

fig_bar = px.bar(
    df,
    x="City",
    y="ESG Score",
    color="ESG Score",
    title="ESG Scores"
)

st.plotly_chart(
    fig_bar,
    use_container_width=True
)

# ---------------- HEATMAP ----------------

st.markdown("## Satellite Methane Heatmap")

fig_map = px.density_mapbox(
    df,
    lat='lat',
    lon='lon',
    z='Methane',
    radius=25,
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

# ---------------- LIVE MAP ----------------

st.markdown("## Live Waste Intelligence Map")

st.map(df[["lat", "lon"]])

# ---------------- PIE CHART ----------------

st.markdown("## Risk Distribution")

risk_counts = df["Risk"].value_counts()

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

# ---------------- TOP DANGEROUS CITIES ----------------

st.markdown("## Top Dangerous Cities")

danger = df.sort_values(
    by="Methane",
    ascending=False
)

st.dataframe(danger)

# ---------------- AI INSIGHTS ----------------

st.markdown("## AI Intelligence Insights")

highest_city = df.loc[
    df["Methane"].idxmax()
]

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

# ---------------- DOWNLOAD REPORT ----------------

csv = df.to_csv(
    index=False
).encode('utf-8')

st.download_button(
    label="Download Intelligence Report",
    data=csv,
    file_name="ZeroWaste_AI_Report.csv",
    mime="text/csv"
)

# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown("""

## ZeroWaste.AI Intelligence Core

Future AI Features:

- Methane hotspot prediction
- Illegal landfill detection
- ESG risk scoring
- Satellite anomaly alerts
- Government intelligence dashboard
- Carbon emission AI
- Smart city intelligence
- Autonomous waste monitoring

""")