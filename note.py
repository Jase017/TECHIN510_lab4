import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load the dataset
df = pd.read_csv("./Data/WineQT.csv")

# Streamlit app layout and title
st.set_page_config(page_title="Wine Quality", page_icon="🍷", layout="centered", initial_sidebar_state="auto")
st.title("🍷 Wine Quality Dataset")
st.markdown("""
            This datasets is related to red variants of the Portuguese "Vinho Verde" wine. The dataset describes the amount of various chemicals present in wine and their effect on its quality.
            """)

quality_slider = st.slider(
    "Alcohol",
    min(df["alcohol"]),
    max(df["alcohol"])
)
df = df[df["alcohol"] == quality_slider]

alcohol_filter = st.selectbox(
    "Wine Quality",
    df["quality"].unique(),
    index = None
)
if alcohol_filter:
    df = df[df['quality'] == alcohol_filter]


st.write(df)

fig = px.histogram(
    df,
    x="fixed acidity"
)
st.plotly_chart(fig)