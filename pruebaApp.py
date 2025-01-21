import streamlit as st
import time

with st.sidebar:
    st.[element_name]

st.button("Ver más", type="primary")



st.write ("Hola mundo")
enable = st.checkbox("Enable camera")
picture = st.camera_input("Take a picture", disabled=not enable)

if picture:
    st.image(picture)





