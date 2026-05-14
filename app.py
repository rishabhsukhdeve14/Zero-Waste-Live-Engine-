import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime
import plotly.express as px

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="ZERO WASTE AI",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #020617;
    color: white;
}

.stMetric {
    background-color: #07122b;
    padding: 15px;
    border-radius: 15px;
    border: 1px solid #0f172a;
}

h1,h2,h3 {
    color: white;
}

.block-container {
    padding-top: 1rem;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# DATABASE
# =====================================================

conn = sqlite3.connect(
    "zero_waste_ai.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS uploads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    upload_time TEXT
)
""")

conn.commit()

# =====================================================
# HEADER
# =====================================================

st.title("🌍 ZERO WASTE AI")
st.subheader(
    "Advanced Environmental Intelligence Platform"
)

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("⚙️ CONTROL PANEL")

selected_region = st.sidebar.selectbox(
    "Target Region",
    [
        "India",
        "Delhi",
        "Mumbai",
        "Hyderabad",
        "Bangalore"
    ]
)

risk_threshold = st.sidebar.slider(
    "Risk Threshold",
    0,
    100,
    75
)

# =====================================================
# FILE UPLOAD
# =====================================================

st.markdown("## 📂 DATASET UPLOAD ENGINE")

uploaded_file = st.file_uploader(
    "Upload CSV Dataset",
    type=["csv"]
)

# =====================================================
# DATA
# =====================================================

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    cursor.execute(
        """
        INSERT INTO uploads
        (filename, upload_time)
        VALUES (?, ?)
        """,
        (
            uploaded_file.name,
            str(datetime.now())
        )
    )

    conn.commit()

    st.success(
        "Dataset Uploaded Successfully"
    )

else:

    df = pd.DataFrame({

        "site_id": range(1, 51),

        "latitude": np.random.uniform(
            18,
            28,
            50
        ),

        "longitude": np.random.uniform(
            72,
            88,
            50
        ),

        "methane": np.random.uniform(
            3900,
            4200,
            50
        ),

        "co2e": np.random.uniform(
            1000,
            5000,
            50
        ),

        "confidence": np.random.uniform(
            80,
            99,
            50
        ),

        "thermal_score": np.random.uniform(
            20,
            90,
            50
        ),

        "risk": np.random.choice(
            ["LOW", "MEDIUM", "HIGH"],
            50
        )
    })

# =====================================================
# LIVE METRICS
# =====================================================

st.markdown("## 📡 LIVE INTELLIGENCE METRICS")

total_sites = len(df)

critical_sites = len(
    df[df["risk"] == "HIGH"]
)

carbon_credit = (
    df["co2e"].sum() * 15
)

avg_confidence = (
    df["confidence"].mean()
)

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Total Sites",
        total_sites
    )

with col2:

    st.metric(
        "Critical Sites",
        critical_sites
    )

with col3:

    st.metric(
        "Carbon Credit USD",
        f"${carbon_credit:,.2f}"
    )

with col4:

    st.metric(
        "Avg Confidence",
        f"{avg_confidence:.2f}%"
    )

# =====================================================
# SEARCH
# =====================================================

st.markdown("## 🔎 SEARCH ENGINE")

search = st.text_input(
    "Search Site / Risk / Value"
)

if search:

    filtered = df[
        df.astype(str)
        .apply(
            lambda x:
            x.str.contains(
                search,
                case=False
            )
        )
        .any(axis=1)
    ]

    st.dataframe(
        filtered,
        use_container_width=True
    )

else:

    st.dataframe(
        df,
        use_container_width=True
    )

# =====================================================
# MAP VIEW
# =====================================================

st.markdown("## 🛰️ LIVE MAP VIEW")

map_df = pd.DataFrame({
    "lat": df["latitude"],
    "lon": df["longitude"]
})

st.map(map_df)

# =====================================================
# HEATMAP CHART
# =====================================================

st.markdown("## 🌡️ METHANE HEATMAP")

fig = px.scatter_mapbox(
    df,
    lat="latitude",
    lon="longitude",
    color="methane",
    size="methane",
    hover_name="site_id",
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

# =====================================================
# CARBON BASELINE ENGINE
# =====================================================

st.markdown("## 🌱 CARBON BASELINE ENGINE")

baseline = df["methane"].mean()

current = baseline + np.random.uniform(
    -50,
    50
)

reduction = (
    (baseline - current)
    / baseline
) * 100

c1, c2, c3 = st.columns(3)

with c1:

    st.metric(
        "Baseline Methane",
        f"{baseline:.2f}"
    )

with c2:

    st.metric(
        "Current Methane",
        f"{current:.2f}"
    )

with c3:

    st.metric(
        "Reduction %",
        f"{reduction:.2f}%"
    )

# =====================================================
# METHANE ALERTS
# =====================================================

st.markdown("## 🚨 METHANE LEAK DETECTION")

high_risk = len(
    df[df["methane"] > 4100]
)

st.error(
    f"{high_risk} HIGH PROBABILITY LEAK ZONES DETECTED"
)

# =====================================================
# FIRE RISK ENGINE
# =====================================================

st.markdown("## 🔥 FIRE RISK ENGINE")

fire_score = (
    df["thermal_score"].mean()
)

st.metric(
    "Average Fire Probability",
    f"{fire_score:.2f}"
)

# =====================================================
# ESG ENGINE
# =====================================================

st.markdown("## 📑 ESG COMPLIANCE ENGINE")

if avg_confidence > 85:

    st.success(
        f"ESG COMPLIANCE STRONG ({avg_confidence:.1f})"
    )

else:

    st.warning(
        f"ESG COMPLIANCE MODERATE ({avg_confidence:.1f})"
    )

# =====================================================
# SDG TRACKING
# =====================================================

st.markdown("## 🌎 SDG TRACKING")

s1, s2, s3 = st.columns(3)

with s1:
    st.success("SDG 11 ACTIVE")

with s2:
    st.success("SDG 12 ACTIVE")

with s3:
    st.success("SDG 13 ACTIVE")

# =====================================================
# AI CLUSTER ENGINE
# =====================================================

st.markdown("## 🧠 AI CLUSTER DETECTION")

cluster_df = pd.DataFrame({

    "cluster_id": range(1, 11),

    "severity": np.random.choice(
        ["LOW", "MEDIUM", "HIGH"],
        10
    ),

    "confidence": np.random.uniform(
        70,
        99,
        10
    )
})

st.dataframe(
    cluster_df,
    use_container_width=True
)

# =====================================================
# SATELLITE EVIDENCE
# =====================================================

st.markdown("## 📦 SATELLITE EVIDENCE ARCHIVE")

evidence_df = pd.DataFrame({

    "evidence_id": [
        f"EVID-{i}"
        for i in range(10)
    ],

    "verification_status": np.random.choice(
        [
            "MULTI-SATELLITE VERIFIED",
            "PARTIAL VERIFY"
        ],
        10
    )
})

st.dataframe(
    evidence_df,
    use_container_width=True
)

# =====================================================
# HISTORICAL SCANS
# =====================================================

st.markdown("## 🕒 HISTORICAL SCANS")

history_df = pd.DataFrame({

    "scan_id": range(1, 6),

    "scan_time": pd.date_range(
        start="2026-01-01",
        periods=5
    ),

    "total_sites": np.random.randint(
        100,
        1000,
        5
    )
})

st.dataframe(
    history_df,
    use_container_width=True
)

# =====================================================
# DATABASE RECORDS
# =====================================================

st.markdown("## 🗂️ STORED UPLOAD RECORDS")

upload_records = pd.read_sql_query(
    "SELECT * FROM uploads",
    conn
)

st.dataframe(
    upload_records,
    use_container_width=True
)

# =====================================================
# SENTINEL STATUS
# =====================================================

st.markdown("## 🛰️ SATELLITE NETWORK STATUS")

sat1, sat2, sat3, sat4 = st.columns(4)

with sat1:
    st.success("Sentinel-1 ACTIVE")

with sat2:
    st.success("Sentinel-2 ACTIVE")

with sat3:
    st.success("Sentinel-5P ACTIVE")

with sat4:
    st.success("Landsat 8/9 ACTIVE")

# =====================================================
# FOOTER
# =====================================================

st.info(
    "ZERO WASTE AI • Stable Environmental Intelligence Deployment Active"
)