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


st.write('Hello')

data_path= 'https://raw.githubusercontent.com/marwaajouz/MSBA325A2/main/smoking2.csv'
data = pd.read_csv(data_path)

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.title('Number of Cigarettes Consumed / Smoking Person / Day / Country')
selected_year = st.slider('Select Year', min_value=data['Year'].min(), max_value=data['Year'].max())
filtered_data = data[data['Year'] == selected_year]
fig = px.bar(filtered_data, x="Country", y="Data.Daily cigarettes",
             text="Data.Daily cigarettes", labels={'Data.Daily cigarettes': 'Cigarettes per Day'})
fig.update_traces(texttemplate='%{text}', textposition='outside')

# Update layout
fig.update_layout(title=f"Number of Cigarettes Consumed / Smoking Person / Day / Country ({selected_year})")

# Show the figure
st.plotly_chart(fig)


