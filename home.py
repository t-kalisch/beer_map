import streamlit as st

from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()
st.write(df)
# Print results.

st.map()
