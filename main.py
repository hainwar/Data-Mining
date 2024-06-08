# Import library yang dibutuhkan
import streamlit as st
from web_functions import load_data

from Tabs import home, predict, visualise

Tabs = {
    "Home": home,
    "Prediction": predict,
    "Visualisation": visualise
}

# Membuat sidebar
st.sidebar.title("Navigasi")

# Membuat radio option
page = st.sidebar.radio("Pages", list(Tabs.keys())) 

# Load dataset
df, x, y = load_data()

# Kondisi call app function
if page in ["Prediction", "Visualisation"]:
    Tabs[page].app(df, x, y)
else:
    Tabs[page].app()
