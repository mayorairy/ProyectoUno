import streamlit as st
import time

pip install streamlit-navigation-bar
from streamlit_navigation_bar import st_navbar

page = st_navbar(["Home", "Documentation", "Examples", "Community", "About"])
st.write(page)

st.button("Ver más", type="primary")



st.write ("Hola mundo")
enable = st.checkbox("Enable camera")
picture = st.camera_input("Take a picture", disabled=not enable)

if picture:
    st.image(picture)





