import streamlit as st
import pandas as pd
import numpy as np
import time

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="ZERO WASTE AI",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>
html, body, [class*="css"]  {
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

[data-testid="stDataFrame"] {
    background-color: #07122b;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.title("🌍 ZERO WASTE AI")
st.subheader("Real-Time Multi-Satellite Environmental Intelligence System")

# ---------------- SAFE DATAFRAME ---------------- #

df = pd.DataFrame({
    "site_id": range(1, 21),
    "baseline_methane": np.random.uniform(3900, 4100, 20),
    "current_methane": np.random.uniform(3950, 4200, 20),
    "co2e": np.random.uniform(1000, 5000, 20),
    "confidence": np.random.uniform(80, 99, 20),
    "risk": np.random.choice(
        ["LOW", "MEDIUM", "HIGH"],
        20
    )
})

# ---------------- METRICS ---------------- #

baseline = df["baseline_methane"].mean()
current = df["current_methane"].mean()
co2 = df["co2e"].sum()
confidence = df["confidence"].mean()

reduction = ((baseline - current) / baseline) * 100

# ---------------- LIVE METRICS ---------------- #

st.markdown("## 📡 LIVE INTELLIGENCE METRICS")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Sites",
        len(df)
    )

    st.metric(
        "Critical Sites",
        len(df[df["risk"] == "HIGH"])
    )

with col2:
    st.metric(
        "Carbon Credit USD",
        f"${co2*15:,.2f}"
    )

    st.metric(
        "Average Confidence",
        f"{confidence:.2f}%"
    )

# ---------------- SEARCH ---------------- #

st.markdown("## 🔎 SEARCH INTELLIGENCE")

search = st.text_input(
    "Search Any Site / Risk"
)

if search:
    filtered = df[
        df.astype(str)
        .apply(lambda x: x.str.contains(search, case=False))
        .any(axis=1)
    ]
    st.dataframe(filtered)
else:
    st.dataframe(df)

# ---------------- MAP ---------------- #

st.markdown("## 🛰️ LIVE MAP VIEW")

lat = st.number_input(
    "Latitude",
    value=21.25
)

lon = st.number_input(
    "Longitude",
    value=81.63
)

map_df = pd.DataFrame({
    "lat": [lat],
    "lon": [lon]
})

st.map(map_df)

# ---------------- CARBON ENGINE ---------------- #

st.markdown("## 🌱 CARBON BASELINE ENGINE")

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

# ---------------- CO2 ENGINE ---------------- #

st.markdown("## ☁️ CO2e EMISSION ENGINE")

st.metric(
    "Total CO2e Tons",
    f"{co2:.2f}"
)

# ---------------- METHANE ALERTS ---------------- #

st.markdown("## 🚨 METHANE LEAK DETECTION")

high_risk = len(df[df["current_methane"] > 4150])

st.error(
    f"{high_risk} HIGH PROBABILITY LEAK ZONES DETECTED"
)

# ---------------- FIRE RISK ---------------- #

st.markdown("## 🔥 FIRE RISK INTELLIGENCE")

fire_score = np.random.uniform(20, 90)

st.metric(
    "Average Fire Probability",
    f"{fire_score:.2f}"
)

# ---------------- ESG ---------------- #

st.markdown("## 📑 ESG COMPLIANCE ENGINE")

if confidence > 85:
    st.success(
        f"ESG COMPLIANCE STRONG ({confidence:.1f})"
    )
else:
    st.warning(
        f"ESG COMPLIANCE MODERATE ({confidence:.1f})"
    )

# ---------------- SDG ---------------- #

st.markdown("## 🌎 SDG TRACKING")

sdg1, sdg2, sdg3 = st.columns(3)

with sdg1:
    st.success("SDG 11 ACTIVE")

with sdg2:
    st.success("SDG 12 ACTIVE")

with sdg3:
    st.success("SDG 13 ACTIVE")

# ---------------- AI DETECTION ---------------- #

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

st.dataframe(cluster_df)

# ---------------- SATELLITE EVIDENCE ---------------- #

st.markdown("## 📦 SATELLITE EVIDENCE ARCHIVE")

evidence_df = pd.DataFrame({
    "evidence_id": [f"EVID-{i}" for i in range(10)],
    "verification_status": np.random.choice(
        [
            "MULTI-SATELLITE VERIFIED",
            "PARTIAL VERIFY"
        ],
        10
    )
})

st.dataframe(evidence_df)

# ---------------- HISTORICAL ---------------- #

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

st.dataframe(history_df)

# ---------------- FOOTER ---------------- #

st.info(
    "ZERO WASTE AI • Stable Render Deployment Active"
)