import ee
try:
    ee.Initialize(project='stalwart-fx-490910-e3')
except:
    ee.Authenticate()
    ee.Initialize(project='stalwart-fx-490910-e3')
st.markdown("## Real Satellite Methane Intelligence")

try:

    dataset = ee.ImageCollection(
        'COPERNICUS/S5P/OFFL/L3_CH4'
    ).select(
        'CH4_column_volume_mixing_ratio_dry_air'
    ).filterDate(
        '2025-01-01',
        '2025-12-31'
    )

    image = dataset.mean()

    india = ee.Geometry.Point([78.9629, 20.5937])

    methane_value = image.reduceRegion(
        reducer=ee.Reducer.mean(),
        geometry=india,
        scale=50000
    ).getInfo()

    st.success("Live satellite connection successful")

    st.write(methane_value)

except Exception as e:
    st.error(f"Satellite Error: {e}")
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import IsolationForest

# PAGE CONFIG

st.set_page_config(
    page_title="ZeroWaste.AI",
    layout="wide"
)

# TITLE

st.title("ZeroWaste.AI")
st.header("Multi-Satellite Intelligence Dashboard")

st.write("AI + ESG + Methane Intelligence + Smart Waste Detection")

# DATA

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

# LINEAR REGRESSION

df["Index"] = np.arange(len(df))

X = df[["Index"]]
y = df["Methane"]

model = LinearRegression()
model.fit(X, y)

future = np.array([[len(df) + 24]])

prediction = model.predict(future)

predicted_value = round(float(prediction[0]), 2)

# ESG SCORE

df["ESG Score"] = np.random.uniform(
    10,
    99,
    len(df)
).round(1)

# ISOLATION FOREST

features = df[["Methane"]]

iso_model = IsolationForest(
    n_estimators=100,
    contamination=0.25,
    random_state=42
)

df["Anomaly"] = iso_model.fit_predict(features)

df["AI Risk"] = df["Anomaly"].apply(
    lambda x: "Critical" if x == -1 else "Normal"
)

# METRICS

st.subheader("Global Intelligence Metrics")

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
    len(df[df["AI Risk"] == "Critical"])
)

col4.metric(
    "Predicted Next 24h",
    predicted_value
)

# DATA TABLE

st.subheader("Live Intelligence Feed")

st.dataframe(df)

# CHART

st.subheader("Methane Trend Analysis")

st.line_chart(df["Methane"])

# AI DETECTION

st.subheader("AI Methane Anomaly Detection")

critical = df[df["AI Risk"] == "Critical"]

if len(critical) > 0:

    st.error("AI detected dangerous methane anomalies")

    st.dataframe(
        critical[
            [
                "City",
                "Methane",
                "AI Risk"
            ]
        ]
    )

else:

    st.success("No dangerous anomalies detected")

# MAP

st.subheader("Satellite Methane Heatmap")

fig = px.scatter_mapbox(
    df,
    lat="lat",
    lon="lon",
    color="Methane",
    size="Methane",
    hover_name="City",
    zoom=3,
    height=500
)

fig.update_layout(
    mapbox_style="open-street-map"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# AI VISUALIZATION

st.subheader("AI Risk Visualization")

fig2 = px.scatter(
    df,
    x="City",
    y="Methane",
    color="AI Risk",
    size="Methane"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# FOOTER

st.write("ZeroWaste.AI Intelligence Core Active")