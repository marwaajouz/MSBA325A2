# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import json
import altair as alt
import squarify
import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt


st.title('Smokers in the Arab Region')
st.write('This page provides insights about the smoking condition in the Arab region using visualizations that show different smoking metrics throughout the years 2000 - 2012')

data_path= 'https://raw.githubusercontent.com/marwaajouz/MSBA325A2/main/smoking2.csv'
data = pd.read_csv(data_path)

st.write('Click the checkbox if you want to see the raw data')
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

