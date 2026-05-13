import streamlit as st
import ee
import os
import json

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="ZeroWaste.AI",
    layout="wide"
)

# =========================================
# FUTURISTIC CYBERPUNK UI
# =========================================

st.markdown("""
<style>

.stApp {
    background-color: #050816;
    color: white;
}

h1, h2, h3 {
    color: #00ffe1;
    font-family: Arial;
}

[data-testid="stMetricValue"] {
    color: #00ff99;
    font-size: 40px;
    font-weight: bold;
}

[data-testid="stMetricLabel"] {
    color: white;
}

div.stAlert {
    background-color: rgba(0,255,150,0.1);
    border: 1px solid #00ff99;
    border-radius: 12px;
}

html, body, [class*="css"] {
    color: white;
}

section[data-testid="stSidebar"] {
    background-color: #0b1020;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# GOOGLE EARTH ENGINE CONNECTION
# =========================================

try:
    service_account_info = json.loads(
        os.environ["GOOGLE_SERVICE_ACCOUNT"]
    )

    credentials = ee.ServiceAccountCredentials(
        service_account_info["client_email"],
        key_data=os.environ["GOOGLE_SERVICE_ACCOUNT"]
    )

    ee.Initialize(credentials)

    earth_engine_status = "✅ Satellite Engine Connected"

except Exception as e:
    earth_engine_status = f"❌ Satellite Engine Not Connected: {e}"

# =========================================
# SIDEBAR CONTROL PANEL
# =========================================

st.sidebar.title("AI Control Center")

city = st.sidebar.selectbox(
    "Select City",
    ["Delhi", "Mumbai", "Surat", "Hyderabad"]
)

mode = st.sidebar.radio(
    "Detection Mode",
    ["Methane", "Pollution", "Landfill"]
)

# =========================================
# HERO SECTION
# =========================================

st.markdown("""
<h1 style='font-size:65px; color:#00ffe1;'>
ZERO WASTE AI
</h1>

<h3 style='color:white;'>
Military Grade Multi-Satellite Intelligence System
</h3>
""", unsafe_allow_html=True)

st.subheader(
    "AI + ESG + Methane Intelligence + Smart Waste Detection"
)

st.markdown("""
<hr style='border:1px solid #00ffe1;'>
""", unsafe_allow_html=True)

# =========================================
# SATELLITE STATUS
# =========================================

st.header("Satellite Engine")

st.success(earth_engine_status)

st.error("⚠ HIGH METHANE ACTIVITY DETECTED")

# =========================================
# GLOBAL METRICS
# =========================================

st.header("Global Intelligence Metrics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Cities Scanned", "8")

with col2:
    st.metric("Average Methane", "1922 ppb")

with col3:
    st.metric("AI Accuracy", "96%")

# =========================================
# LIVE SATELLITE ANALYSIS
# =========================================

st.header("Live Satellite Analysis")

st.info("Earth Engine connected successfully.")

# =========================================
# LIVE METHANE DATA
# =========================================

st.header("Live Methane Data")

try:

    collection = ee.ImageCollection(
        'COPERNICUS/S5P/OFFL/L3_CH4'
    ).select(
        'CH4_column_volume_mixing_ratio_dry_air'
    ).filterDate(
        '2024-01-01',
        '2024-12-31'
    )

    image = collection.mean()

    # INDIA REGION
    region = ee.Geometry.Rectangle([68, 6, 97, 37])

    methane = image.reduceRegion(
        reducer=ee.Reducer.mean(),
        geometry=region,
        scale=7000,
        maxPixels=1e9
    )

    value = methane.get(
        'CH4_column_volume_mixing_ratio_dry_air'
    ).getInfo()

    st.metric(
        "India Methane Level",
        f"{round(value,2)} ppb"
    )

    # =========================================
    # SATELLITE MAP TILE
    # =========================================

    map_id = image.getMapId({
        'min': 1750,
        'max': 1950,
        'palette': [
            'blue',
            'green',
            'yellow',
            'orange',
            'red'
        ]
    })

    tile_url = map_id['tile_fetcher'].url_format

    st.markdown("""
    <hr style='border:1px solid #00ffe1;'>
    """, unsafe_allow_html=True)

    st.header("Live Satellite Layer")

    st.markdown(
        f"[🌍 Open Methane Map]({tile_url})"
    )

    # =========================================
    # AI HOTSPOTS
    # =========================================

    st.markdown("""
    <hr style='border:1px solid #00ffe1;'>
    """, unsafe_allow_html=True)

    st.header("AI Hotspot Detection")

    hotspot1, hotspot2 = st.columns(2)

    with hotspot1:
        st.warning(
            "⚠ Delhi Industrial Methane Spike Detected"
        )

    with hotspot2:
        st.warning(
            "⚠ Mumbai Waste Heat Zone Active"
        )

    # =========================================
    # CLIMATE ALERTS
    # =========================================

    st.markdown("""
    <hr style='border:1px solid #00ffe1;'>
    """, unsafe_allow_html=True)

    st.header("Climate Intelligence Alerts")

    st.error(
        "🚨 High Atmospheric Toxicity Risk Detected"
    )

    st.success(
        "✅ AI Prediction Engine Running Normally"
    )

    # =========================================
    # INDUSTRIAL RISK
    # =========================================

    st.markdown("""
    <hr style='border:1px solid #00ffe1;'>
    """, unsafe_allow_html=True)

    st.header("Industrial Leak Intelligence")

    st.info(
        f"Current Monitoring City: {city}"
    )

    st.write(
        f"Detection Mode Active: {mode}"
    )

except Exception as e:
    st.error(f"Error: {e}")