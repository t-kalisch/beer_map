import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read()

for row in df.itertuples():
  st.write(f"{row.name} has a :{row.pet}:")

st.write("Hello")

st.map()
