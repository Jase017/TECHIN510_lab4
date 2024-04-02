import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv("./Data/WineQT.csv")

st.set_page_config(page_title="Wine Quality", 
                   page_icon="🍷",
                   layout="centered", 
                   initial_sidebar_state="auto")
st.title("🍷 Wine Quality Dataset")
st.markdown("""
            This datasets is related to red variants of the Portuguese "Vinho Verde" wine. The dataset describes the amount of various chemicals present in wine and their effect on its quality.
            """)


quality = st.sidebar.selectbox('Select Wine Quality', options=[f"All Qualities"] + sorted(df['quality'].unique().tolist()))
if quality != "All Qualities":
    df = df[df['quality'] == quality]


min_alcohol, max_alcohol = st.sidebar.slider('Select a range of alcohol content',
                                             float(df['alcohol'].min()),
                                             float(df['alcohol'].max()),
                                             (float(df['alcohol'].min()), float(df['alcohol'].max())))
df = df[(df['alcohol'] >= min_alcohol) & (df['alcohol'] <= max_alcohol)]


with st.expander("Raw Data"):
    st.write(df)

fig = px.scatter(
    df,
    x = "fixed acidity",
    y = "residual sugar"
)
st.plotly_chart(fig)

