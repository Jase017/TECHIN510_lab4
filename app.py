import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("./Data/WineQT.csv")

st.set_page_config(page_title="Wine Quality", 
                   page_icon="🍷",
                   layout="centered", 
                   initial_sidebar_state="auto")

st.title("🍷 Wine Quality Dataset")

st.markdown("""
            This datasets is related to red variants of the Portuguese :red[🍷"Vinho Verde"] wine. The dataset describes the amount of various chemicals present in wine and their effect on its quality.
            """)

quality = st.sidebar.selectbox(
    'Select Wine Quality', options=["All Qualities"] + sorted(df['quality'].unique().tolist())
)
if quality != "All Qualities":
    df = df[df['quality'] == int(quality)]

min_alcohol, max_alcohol = st.sidebar.slider('Select a range of alcohol content',
                                             float(df['alcohol'].min()),
                                             float(df['alcohol'].max()),
                                             (float(df['alcohol'].min()), float(df['alcohol'].max())))
df = df[(df['alcohol'] >= min_alcohol) & (df['alcohol'] <= max_alcohol)]

chart_type = st.sidebar.selectbox(
    "Select Chart Type", 
    options=["Scatter Plot", "Bar Chart", "3D Scatter", "Parallel Categories"]
)

with st.expander("Raw Data"):
    st.write(df)

if chart_type == "Scatter Plot":
        fig1 = px.scatter(df, x="fixed acidity", y="residual sugar")
        st.plotly_chart(fig1)
elif chart_type == "Bar Chart":
        fig1 = px.bar(df, x="quality", y="alcohol")
        st.plotly_chart(fig1)
elif chart_type == "3D Scatter":
        fig1 = px.scatter_3d(df, x='alcohol', y='fixed acidity', z='residual sugar',
        color='quality')
        st.plotly_chart(fig1)
elif chart_type == "Parallel Categories":
        fig1 = fig = px.parallel_categories(df)
        st.plotly_chart(fig1)