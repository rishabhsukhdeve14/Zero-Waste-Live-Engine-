import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Waste.Ai", layout="wide")

st.title("🚀 Waste.Ai")
st.subheader("♻️ Multi-Satellite Intelligence Dashboard")

uploaded_file = st.file_uploader(
    "Upload CSV / TXT / XLSX",
    type=["csv", "txt", "xlsx"]
)

df = None

if uploaded_file is not None:

    st.success(f"✅ Uploaded: {uploaded_file.name}")

    try:

        # CSV
        if uploaded_file.name.endswith(".csv"):

            try:
                df = pd.read_csv(uploaded_file)

            except:
                uploaded_file.seek(0)

                df = pd.read_csv(
                    uploaded_file,
                    encoding="latin1"
                )

        # TXT
        elif uploaded_file.name.endswith(".txt"):

            df = pd.read_csv(
                uploaded_file,
                sep=None,
                engine="python"
            )

        # XLSX
        elif uploaded_file.name.endswith(".xlsx"):

            df = pd.read_excel(uploaded_file)

    except Exception as e:

        st.error(f"❌ Error reading file: {e}")

# =========================
# SHOW DATA
# =========================

if df is not None:

    st.markdown("## 📊 Live Data Preview")

    st.dataframe(
        df.head(100),
        use_container_width=True
    )

    st.markdown("## 📈 Dataset Stats")

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", len(df))
    col2.metric("Columns", len(df.columns))
    col3.metric(
        "Memory MB",
        round(df.memory_usage().sum()/1024/1024, 2)
    )

    # Numeric columns
    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) > 0:

        selected_col = st.selectbox(
            "Select Numeric Column",
            numeric_cols
        )

        fig