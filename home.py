import streamlit as st
import geopandas as gpd
import geopy
import pandas as pd
import numpy
import pandasql as pdsql
from streamlit_gsheets import GSheetsConnection

from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(ttl="10m")
st.write(df)
# Print results
st.map(data = df)

#def check_in(street, city, country, df, conn):


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
  conn.clear(worksheet="0")
  #st.cache_data.clear()

geolocator = Nominatim(user_agent="GTA Lookup")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
location = geolocator.geocode(street+", "+city+", "+country)
st.write(location)
lat = location.latitude
lon = location.longitude

map_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})

st.map(map_data) 
