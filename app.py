import streamlit as st
import seaborn as sns
import pandas as pd

st.set_page_config(
    page_title = "Wine Quality",
    page_icon = "🍷",
    layout = "centered",
    initial_sidebar_state = "auto",
    menu_items = None
)
st.title("🍷 Wine Quality Dataset")
st.markdown("""
            This datasets is related to red variants of the Portuguese :red["Vinho Verde🍷"] wine. The dataset describes the amount of various chemicals present in wine and their effect on it's quality.
""")
df = pd.read_csv("./Data/WineQT.csv")
start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'blue'))
st.write(df)