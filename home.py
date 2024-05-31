import streamlit as st
import geopandas as gpd
import geopy
import pandas as pd
import numpy
import pandasql as pdsql
from streamlit_gsheets import GSheetsConnection

from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import folium

import plotly.express as px


# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(ttl="1m")
#st.write(df)
df = df.dropna()
st.write(df)
# Print results


#def check_in(street, city, country, df, conn):


import folium

m = folium.Map(location=[45.5236, -122.6750])
m

st.map(data = df, use_container_width=True)

street = st.sidebar.text_input("Street")
city = st.sidebar.text_input("City")
country = st.sidebar.text_input("Country")
input = st.sidebar.button("Check in", key="input")#, on_click=check_in, args=(street, city, country, df, conn))
if input:
  geolocator = Nominatim(user_agent="GTA Lookup")
  geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
  location = geolocator.geocode(street+", "+city+", "+country)

  lat = location.latitude
  lon = location.longitude
  st.write(lat, lon)

  df = df.append({'lat': lat, 'lon': lon}, ignore_index=True)
  st.write(df)
  conn.update(data=df)
  #st.cache_data.clear()

fig = px.scatter_geo(
    data_frame=df,
    #color="color_column",
    lon="lon",
    lat="lat",
    #projection="natural earth",
    #hover_name="hover_column",
    size="size",  # <-- Set the column name for size
    height=800,
)

st.plotly_chart(fig, use_container_width=True)
