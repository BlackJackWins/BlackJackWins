import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="NEW Javier App",
                    page_icon = ":bar_chart:",
                    layout="wide")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")