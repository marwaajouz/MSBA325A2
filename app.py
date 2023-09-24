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






