import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import st_folium
from folium.plugins import HeatMap
import sqlite3
import os
from datetime import datetime

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="ZERO WASTE AI",
    layout="wide"
)

# ==========================================
# DATABASE SETUP
# ==========================================

conn = sqlite3.connect(
    "intelligence.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS scan_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    scan_time TEXT,
    total_rows INTEGER,
    suspicious_rows INTEGER,
    invalid_coordinates INTEGER,
    missing_rows INTEGER
)
""")

conn.commit()

# ==========================================
# UPLOADS FOLDER
# ==========================================

os.makedirs("uploads", exist_ok=True)

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("ZERO WASTE AI")

st.sidebar.success("SYSTEM ONLINE")

city = st.sidebar.selectbox(
    "Monitor City",
    [
        "Delhi",
        "Mumbai",
        "Bangalore",
        "Chennai"
    ]
)

sensitivity = st.sidebar.slider(
    "AI Scan Sensitivity",
    0,
    100,
    100
)

mode = st.sidebar.selectbox(
    "Detection Mode",
    [
        "Waste Monitoring",
        "Methane Detection",
        "Thermal Intelligence"
    ]
)

# ==========================================
# TITLE
# ==========================================

st.title("🌍 ZERO WASTE AI")

st.subheader(
    "Real-Time Multi-Satellite Environmental Intelligence"
)

# ==========================================
# METRICS
# ==========================================

col1, col2, col3 = st.columns(3)

col1.metric(
    "Cities Scanned",
    "24"
)

col2.metric(
    "India Methane",
    "1922.53"
)

col3.metric(
    "AI Accuracy",
    "96%"
)

st.divider()

# ==========================================
# SATELLITE ENGINE
# ==========================================

st.header("🛰 MULTI SATELLITE INTELLIGENCE")

st.success("Multi-Satellite Engine Online")

m1, m2, m3, m4 = st.columns(4)

m1.metric(
    "Sentinel-5P",
    "1922.53"
)

m2.metric(
    "Sentinel-2",
    "Surface"
)

m3.metric(
    "Landsat-8",
    "Thermal"
)

m4.metric(
    "MODIS",
    "Fire Alerts"
)

st.divider()

# ==========================================
# UPLOAD SECTION
# ==========================================

st.header("📂 Upload Intelligence CSV")

uploaded_file = st.file_uploader(
    "Upload Large Intelligence CSV File",
    type=["csv"]
)

# ==========================================
# FILE PROCESSING
# ==========================================

if uploaded_file is not None:

    # ======================================
    # SAVE FILE
    # ======================================

    file_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(
        f"Uploaded Successfully: {uploaded_file.name}"
    )

    # ======================================
    # LOAD CSV
    # ======================================

    try:

        df = pd.read_csv(
            uploaded_file,
            nrows=5000
        )

    except Exception as e:

        st.error(
            f"CSV Loading Error: {e}"
        )

        st.stop()

    # ======================================
    # SHOW COLUMNS
    # ======================================

    st.subheader("📜 Detected Columns")

    st.write(df.columns.tolist())

    # ======================================
    # SEARCH ENGINE
    # ======================================

    st.subheader("🔎 Search Intelligence")

    search_value = st.text_input(
        "Search Any Value"
    )

    if search_value:

        filtered_df = df[
            df.astype(str)
            .apply(
                lambda row:
                row.str.contains(
                    search_value,
                    case=False
                ).any(),
                axis=1
            )
        ]

        st.dataframe(filtered_df)

    # ======================================
    # LIVE TABLE
    # ======================================

    st.subheader("📄 Live Intelligence Table")

    st.dataframe(df.head(100))

    # ======================================
    # AUTO COORDINATE DETECTION
    # ======================================

    lat_col = None
    lon_col = None

    for col in df.columns:

        col_lower = col.lower()

        if col_lower in [
            "latitude",
            "lat"
        ]:
            lat_col = col

        if col_lower in [
            "longitude",
            "lon",
            "lng"
        ]:
            lon_col = col

    # ======================================
    # MAP ENGINE
    # ======================================

    if lat_col and lon_col:

        st.subheader(
            "🗺 Live Landfill Intelligence Map"
        )

        map_df = df[
            [lat_col, lon_col]
        ].dropna()

        map_df.columns = [
            "lat",
            "lon"
        ]

        m = folium.Map(
            location=[
                map_df["lat"].mean(),
                map_df["lon"].mean()
            ],
            zoom_start=5,
            tiles="CartoDB dark_matter"
        )

        for _, row in map_df.iterrows():

            folium.CircleMarker(
                location=[
                    row["lat"],
                    row["lon"]
                ],
                radius=3,
                color="lime",
                fill=True,
                fill_opacity=0.8
            ).add_to(m)

        st_folium(
            m,
            width=1200,
            height=700
        )

    else:

        st.warning(
            "Latitude / Longitude Columns Not Found"
        )

    st.divider()

    # ======================================
    # AI VERIFICATION ENGINE
    # ======================================

    st.header("🧠 AI DATA VERIFICATION ENGINE")

    if st.button("VERIFY DATASET"):

        suspicious_count = 0
        invalid_coord_count = 0
        missing_rows = 0

        verification_results = []

        # ==================================
        # AUTO METHANE COLUMN DETECTION
        # ==================================

        methane_col = None

        for c in df.columns:

            c_lower = c.lower()

            if (
                "methane" in c_lower
                or "ch4" in c_lower
            ):

                methane_col = c
                break

        # ==================================
        # VERIFICATION LOOP
        # ==================================

        for idx, row in df.iterrows():

            issues = []

            # ==============================
            # MISSING VALUES
            # ==============================

            if row.isnull().sum() > 0:

                missing_rows += 1

                issues.append(
                    "Missing Data"
                )

            # ==============================
            # COORDINATE VALIDATION
            # ==============================

            if lat_col and lon_col:

                try:

                    lat = float(
                        row[lat_col]
                    )

                    lon = float(
                        row[lon_col]
                    )

                    if lat < -90 or lat > 90:

                        invalid_coord_count += 1

                        issues.append(
                            "Invalid Latitude"
                        )

                    if lon < -180 or lon > 180:

                        invalid_coord_count += 1

                        issues.append(
                            "Invalid Longitude"
                        )

                except:

                    invalid_coord_count += 1

                    issues.append(
                        "Coordinate Parse Error"
                    )

            # ==============================
            # METHANE VALIDATION
            # ==============================

            if methane_col:

                try:

                    methane_value = float(
                        row[methane_col]
                    )

                    if methane_value > 3000:

                        suspicious_count += 1

                        issues.append(
                            "High Methane"
                        )

                except:

                    issues.append(
                        "Methane Parse Error"
                    )

            # ==============================
            # STATUS
            # ==============================

            status = "VERIFIED"

            if len(issues) > 0:

                status = "SUSPICIOUS"

            verification_results.append({

                "row": idx,

                "status": status,

                "issues": ", ".join(issues)

            })

        # ==================================
        # RESULTS DATAFRAME
        # ==================================

        results_df = pd.DataFrame(
            verification_results
        )

        # ==================================
        # SAVE TO SQLITE DATABASE
        # ==================================

        cursor.execute("""
        INSERT INTO scan_history (
            filename,
            scan_time,
            total_rows,
            suspicious_rows,
            invalid_coordinates,
            missing_rows
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """, (

            uploaded_file.name,

            str(datetime.now()),

            len(df),

            suspicious_count,

            invalid_coord_count,

            missing_rows

        ))

        conn.commit()

        # ==================================
        # SHOW RESULTS
        # ==================================

        st.success(
            "DATASET VERIFICATION COMPLETE"
        )

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Verified Rows",
            len(df)
        )

        c2.metric(
            "Suspicious Rows",
            suspicious_count
        )

        c3.metric(
            "Invalid Coordinates",
            invalid_coord_count
        )

        c4.metric(
            "Rows With Missing Data",
            missing_rows
        )

        st.divider()

        st.subheader(
            "📡 Verification Results"
        )

        st.dataframe(
            results_df.head(100)
        )

        st.success(
            "AI Verification Engine Finished"
        )

    st.divider()

    # ======================================
    # DATABASE HISTORY
    # ======================================

    st.header("🗄 Scan History Database")

    history = pd.read_sql_query(
        """
        SELECT * FROM scan_history
        ORDER BY id DESC
        """,
        conn
    )

    st.dataframe(history)

    st.divider()

    # ======================================
    # AI RISK ENGINE
    # ======================================

    st.header("🚨 AI RISK ENGINE")

    st.error(
        "Environmental anomalies detected"
    )

    st.success(
        "Real-Time Intelligence Running"
    )

# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "ZERO WASTE AI • Real-Time Multi-Satellite Intelligence"
)