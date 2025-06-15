import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium

# Load dataset (replace this with your merged dataset if local)
df = pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv", 
                 usecols=["location", "date", "new_cases", "total_cases", 
                          "new_deaths", "total_deaths"])
df['date'] = pd.to_datetime(df['date'])

st.title("🌍 COVID-19 Interactive Dashboard")

# Filters
countries = st.multiselect("Select Countries", df['location'].unique(), default=["India", "United States"])
date_range = st.date_input("Select Date Range", [df['date'].min(), df['date'].max()])
filtered = df[(df['location'].isin(countries)) & (df['date'].between(*date_range))]

# Plotting Cases
st.subheader("📈 New Cases Over Time")
fig = px.line(filtered, x="date", y="new_cases", color="location", title="New COVID-19 Cases")
st.plotly_chart(fig)

st.subheader("💀 Deaths Over Time")
fig2 = px.line(filtered, x="date", y="new_deaths", color="location", title="COVID-19 Deaths")
st.plotly_chart(fig2)
