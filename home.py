import streamlit as st
import geopandas as gpd
import geopy
import pandas as pd
from streamlit_gsheets import GSheetsConnection

from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(ttl=0)
st.write(df)
# Print results

st.map(data = df)




street = st.sidebar.text_input("Street", "75 Bay Street")
city = st.sidebar.text_input("City", "Toronto")
country = st.sidebar.text_input("Country", "Canada")

geolocator = Nominatim(user_agent="GTA Lookup")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
location = geolocator.geocode(street+", "+city+", "+country)
st.write(location)
lat = location.latitude
lon = location.longitude

map_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})

st.map(map_data) 
