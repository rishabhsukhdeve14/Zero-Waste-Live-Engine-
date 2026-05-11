import streamlit as st
import pandas as pd

st.title("Zero Waste Live Engine")

df = pd.read_csv("live_methane_data.csv", header=None)

st.write("Live Landfill Monitoring")

st.dataframe(df)