import streamlit as st
import pandas as pd
import folium
import plotly.express as px

from streamlit_folium import st_folium

st.set_page_config(
    page_title="Waste.Ai",
    layout="wide"
)

# TITLE
st.title("🚀 Waste.Ai")

st.subheader(
    "♻️ Multi-Satellite Live Monitoring Engine"
)

# LOAD CSV
df = pd.read_csv(
    "live_methane_data.csv",
    header=None
)

# FIX EXTRA COLUMNS
df = df.iloc[:, :8]

# COLUMN NAMES
df.columns = [
    "Timestamp",
    "Landfill_ID",
    "State",
    "City",
    "Latitude",
    "Longitude",
    "Methane",
    "Satellite"
]

# CLEAN DATA
df["Methane"] = pd.to_numeric(
    df["Methane"],
    errors="coerce"
)

df["Latitude"] = pd.to_numeric(
    df["Latitude"],
    errors="coerce"
)

df["Longitude"] = pd.to_numeric(
    df["Longitude"],
    errors="coerce"
)

df = df.dropna()

# LIVE TABLE
st.subheader("📡 Live Landfill Sites")

st.dataframe(df)
# =========================
# AI RISK ENGINE
# =========================

def get_risk(methane):

    if methane < 1900:
        return "🟢 LOW"

    elif methane < 2050:
        return "🟡 MEDIUM"

    elif methane < 2150:
        return "🟠 HIGH"

    else:
        return "🔴 CRITICAL"


# Add Risk Column
df["Risk_Level"] = df["Methane"].apply(get_risk)

# =========================
# AI RISK TABLE
# =========================

st.subheader("🚨 AI Risk Detection")

st.dataframe(
    df[
        [
            "City",
            "Methane",
            "Risk_Level"
        ]
    ].sort_values(
        by="Methane",
        ascending=False
    )
)

# =========================
# RISK SUMMARY
# =========================

critical_count = len(df[df["Risk_Level"] == "🔴 CRITICAL"])
high_count = len(df[df["Risk_Level"] == "🟠 HIGH"])
medium_count = len(df[df["Risk_Level"] == "🟡 MEDIUM"])
low_count = len(df[df["Risk_Level"] == "🟢 LOW"])

st.subheader("📊 AI Risk Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("🔴 Critical", critical_count)
col2.metric("🟠 High", high_count)
col3.metric("🟡 Medium", medium_count)
col4.metric("🟢 Low", low_count)

# =========================
# TOP CRITICAL ALERTS
# =========================

critical_sites = df[df["Risk_Level"] == "🔴 CRITICAL"]

st.subheader("🚨 Critical Methane Alerts")

st.dataframe(
    critical_sites.sort_values(
        by="Methane",
        ascending=False
    )
)

# STATS
st.subheader("📊 Monitoring Stats")

col1, col2 = st.columns(2)

col1.metric(
    "Total Sites",
    len(df)
)

col2.metric(
    "Highest Methane",
    int(df["Methane"].max())
)

# TOP ALERTS
st.subheader("🚨 Top Methane Alerts")

top_sites = df.sort_values(
    by="Methane",
    ascending=False
).head(10)

st.dataframe(top_sites)

# LIVE MAP
st.subheader("🗺️ Live Landfill Map")

m = folium.Map(
    location=[22.5, 80.0],
    zoom_start=5
)

# MAP MARKERS
for _, row in df.iterrows():

    methane = row["Methane"]

    if methane > 2100:
        color = "red"

    elif methane > 1950:
        color = "orange"

    else:
        color = "green"

    folium.CircleMarker(
        location=[
            row["Latitude"],
            row["Longitude"]
        ],

        radius=10,

        popup=f"""
        <b>City:</b> {row['City']}<br>
        <b>State:</b> {row['State']}<br>
        <b>Methane:</b> {methane}<br>
        <b>Satellite:</b> {row['Satellite']}
        """,

        color=color,
        fill=True,
        fill_color=color

    ).add_to(m)

# SHOW MAP
st_folium(
    m,
    width=1200,
    height=600
)

# LIVE TREND GRAPH
st.subheader("📈 Methane Trend Analysis")

fig = px.line(
    df,
    x="Timestamp",
    y="Methane",
    color="City",
    title="Live Methane Emission Trends"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
# =========================
# PDF INTELLIGENCE ENGINE
# =========================

import pdfplumber

st.subheader("📄 Upload Rare Intelligence PDF")

uploaded_pdf = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_pdf is not None:

    full_text = ""

    with pdfplumber.open(uploaded_pdf) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if text:
                full_text += text + "\n"

    st.subheader("🧠 Extracted Intelligence")

    st.text_area(
        "PDF Data",
        full_text,
        height=400
    )
import streamlit as st
import pandas as pd
import os

st.title("🚀 Waste.Ai Upload Center")

uploaded_file = st.file_uploader(
    "Upload Any File",
    type=["pdf", "csv", "xlsx", "txt", "png", "jpg", "jpeg", "geojson"]
)

if uploaded_file is not None:

    save_path = os.path.join("uploads", uploaded_file.name)

    os.makedirs("uploads", exist_ok=True)

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"✅ File Uploaded: {uploaded_file.name}")

    # CSV Preview
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
        st.subheader("📊 CSV Preview")
        st.dataframe(df)

    # TXT Preview
    elif uploaded_file.name.endswith(".txt"):
        text = uploaded_file.read().decode("utf-8")
        st.subheader("📄 Text Preview")
        st.text(text[:5000])

    # PDF Info
    elif uploaded_file.name.endswith(".pdf"):
        st.subheader("📕 PDF Uploaded Successfully")
        st.write("PDF saved in uploads folder.")

    # Image Preview
    elif uploaded_file.name.endswith((".png", ".jpg", ".jpeg")):
        st.image(uploaded_file)

    else:
        st.info("File uploaded successfully.")
# CSV ANALYSIS

if uploaded_file is not None:

    if uploaded_file.name.endswith(".csv"):

        try:
            df = pd.read_csv(uploaded_file)

            st.subheader("📊 Uploaded Data Preview")
            st.dataframe(df)

            st.subheader("📈 Dataset Insights")

            col1, col2, col3 = st.columns(3)

            col1.metric("Rows", len(df))
            col2.metric("Columns", len(df.columns))
            col3.metric("Missing Values", df.isnull().sum().sum())

            st.subheader("🧠 Column Names")
            st.write(df.columns.tolist())

            st.subheader("📉 Basic Statistics")
            st.write(df.describe())

        except Exception as e:
            st.error(f"Error reading CSV: {e}")
if uploaded_file is not None:

    if uploaded_file.name.endswith(".csv"):

        try:
            df = pd.read_csv(uploaded_file, low_memory=False)

            st.subheader("📊 CSV Preview")
            st.dataframe(df.head(100))

            st.subheader("📈 Dataset Insights")

            col1, col2, col3 = st.columns(3)

            col1.metric("Rows", len(df))
            col2.metric("Columns", len(df.columns))
            col3.metric("Missing Values", df.isnull().sum().sum())

            st.subheader("🧠 Column Names")
            st.write(df.columns.tolist())

        except Exception as e:
            st.error(f"Error reading CSV: {e}")