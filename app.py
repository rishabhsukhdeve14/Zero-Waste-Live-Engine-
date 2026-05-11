import streamlit as st
import pandas as pd

st.title("Zero Waste Live Engine")

st.subheader("Live Landfill Monitoring")

df = pd.read_csv(
    "live_methane_data.csv",
    header=None,
    names=[
        "Timestamp",
        "Landfill ID",
        "State",
        "City",
        "Latitude",
        "Longitude",
        "Methane",
        "Source"
    ]
)

st.dataframe(df)

st.subheader("Top Methane Sites")

top_sites = df.sort_values(by="Methane", ascending=False)

st.dataframe(top_sites.head(20))