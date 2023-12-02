import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    column = st.selectbox("Choose a column", data.columns)
    if st.button("Plot"):
        st.hist(data[column])
