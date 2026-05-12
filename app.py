import streamlit as st
import pandas as pd
import io
import os

# ========================================
# PAGE CONFIG
# ========================================

st.set_page_config(
    page_title="Waste.Ai",
    layout="wide"
)

# ========================================
# TITLE
# ========================================

st.title("🚀 Waste.Ai")
st.subheader("♻️ Multi-Satellite Live Monitoring Engine")

# ========================================
# PDF UPLOAD SECTION
# ========================================

st.header("📄 Upload Rare Intelligence PDF")

pdf_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if pdf_file is not None:

    os.makedirs("uploads", exist_ok=True)

    pdf_path = os.path.join("uploads", pdf_file.name)

    with open(pdf_path, "wb") as f:
        f.write(pdf_file.getbuffer())

    st.success(f"✅ PDF Uploaded: {pdf_file.name}")

# ========================================
# CSV / FILE UPLOAD SECTION
# ========================================

st.header("🚀 Waste.Ai Upload Center")

uploaded_file = st.file_uploader(
    "Upload Any File",
    type=["csv", "txt", "xlsx", "pdf"]
)

# ========================================
# FILE ANALYSIS
# ========================================

if uploaded_file is not None:

    st.success(f"✅ File Uploaded: {uploaded_file.name}")

    # ====================================
    # CSV FILE
    # ====================================

    if uploaded_file.name.endswith(".csv"):

        try:

            # READ SMALL PART OF LARGE FILE
            content = uploaded_file.getvalue().decode(
                "utf-8",
                errors="ignore"
            )

            # TAKE FIRST 100 LINES
            lines = content.splitlines()[:100]

            small_csv = "\n".join(lines)

            df = pd.read_csv(
                io.StringIO(small_csv),
                on_bad_lines='skip'
            )

            # PREVIEW
            st.subheader("📊 CSV Preview")

            st.dataframe(df)

            # DATASET INFO
            st.subheader("📈 Dataset Insights")

            col1, col2, col3 = st.columns(3)

            col1.metric("Rows", df.shape[0])
            col2.metric("Columns", df.shape[1])
            col3.metric(
                "Missing Values",
                int(df.isnull().sum().sum())
            )

            # COLUMN NAMES
            st.subheader("🧠 Column Names")

            st.write(df.columns.tolist())

            # RAW DATA
            st.subheader("🔥 Raw Data")

            st.text(content[:5000])

        except Exception as e:

            st.error(f"CSV Error: {e}")

    # ====================================
    # TXT FILE
    # ====================================

    elif uploaded_file.name.endswith(".txt"):

        text = uploaded_file.read().decode(
            "utf-8",
            errors="ignore"
        )

        st.subheader("📄 TXT Preview")

        st.text(text[:5000])

    # ====================================
    # PDF FILE
    # ====================================

    elif uploaded_file.name.endswith(".pdf"):

        st.subheader("📕 PDF Uploaded Successfully")

        st.write("PDF stored in uploads folder.")

# ========================================
# AI SECTION
# ========================================

st.header("🧠 Waste.Ai Intelligence Engine")

st.info("""
Future AI Features:
- Methane hotspot prediction
- Illegal landfill detection
- ESG risk scoring
- Satellite anomaly alerts
- Government intelligence dashboard
""")

# ========================================
# FOOTER
# ========================================

st.caption("Waste.Ai © 2026")