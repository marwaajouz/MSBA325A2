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

st.subheader('Number of Cigarettes Consumed / Smoking Person / Day / Country')
# Create a Streamlit slider to select the year
selected_year = st.slider('Select Year', 2000, 2012)

# Filter data for the selected year
filtered_data = data[data['Year'] == selected_year]

# Create a bar chart using Matplotlib
fig, ax = plt.subplots()
ax.bar(filtered_data["Country"], filtered_data["Data.Daily cigarettes"])
ax.set_xlabel("Country")
ax.set_ylabel("Cigarettes per Day")
ax.set_title(f"Number of Cigarettes Consumed / Smoking Person / Day / Country ({selected_year})")

plt.xticks(rotation=90)
# Display the chart in Streamlit
st.pyplot(fig)


st.subheader('Country Data Visualizer')

selected_country = st.selectbox('Select a country', data['Country'].unique())

# Radio button for selecting 'percentage' or 'numbers'
data_type = st.radio('Select data type', ['percentage', 'numbers'])
filtered_data = data[data['Country'] == selected_country]

colors = ['blue', 'red']

plt.figure(figsize=(10, 6))

if data_type == 'percentage':
    plt.plot(filtered_data['Year'], filtered_data['Data.Percentage.Male'], label='Male Percentage', color=colors[0])
    plt.plot(filtered_data['Year'], filtered_data['Data.Percentage.Female'], label='Female Percentage', color=colors[1])
    plt.ylabel('Percentage')
    plt.title(f'{selected_country} Percentage Data')
else:
    plt.plot(filtered_data['Year'], filtered_data['Data.Smokers.Male'], label='Male Smokers', color=colors[0])
    plt.plot(filtered_data['Year'], filtered_data['Data.Smokers.Female'], label='Female Smokers', color=colors[1])
    plt.ylabel('Number of Smokers')
    plt.title(f'{selected_country} Number of Smokers')

plt.xlabel('Year')
plt.legend()
st.pyplot(plt)

