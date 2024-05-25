import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read()
st.write(df)
for row in df.itertuples():
  st.write(f"{row.lat} has a :{row.long}:")

st.write("Hello")

st.map()
