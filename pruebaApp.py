import streamlit as st
import time
st.write ("Hola mundo")

enable = st.checkbox("Activar camera")
picture = st.camera_input("Take a picture", disabled=not enable)

if picture:
    st.image(picture)




