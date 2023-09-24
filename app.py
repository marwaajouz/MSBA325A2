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



fig, ax = plt.subplots()
bars = ax.bar(filtered_data["Country"], filtered_data["Data.Daily cigarettes"])
ax.set_xlabel("Country")
ax.set_ylabel("Cigarettes per Day")
ax.set_title(f"Number of Cigarettes Consumed / Smoking Person / Day / Country ({selected_year})")

# Add interactivity to display data on hover
def display_hover_data(event):
    for bar in bars:
        cont, ind = bar.contains(event)
        if cont:
            x = bar.get_x()
            y = bar.get_height()
            country = bar.get_label()
            plt.gca().text(x, y, f"{country}: {y}", ha="center", va="bottom", fontsize=10)

fig.canvas.mpl_connect("motion_notify_event", display_hover_data)

# Display the chart in Streamlit
st.pyplot(fig)


# Create an Altair chart
chart = alt.Chart(filtered_data).mark_bar().encode(
    x="Country",
    y="Data.Daily cigarettes",
    text="Data.Daily cigarettes"
).properties(
    title=f"Number of Cigarettes Consumed per Smoking Person per Day in {selected_year}"
)

# Show the chart in Streamlit
st.altair_chart(chart, use_container_width=True)

