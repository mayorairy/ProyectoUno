import streamlit as st
import time

col1, col2, col3 = st.columns(3)

with col1:
    st.header("¿Qúe es la discapacidad?")
    st.image("https://i.pinimg.com/736x/cf/66/33/cf66334166ddd4c120148dc07c492449.jpg")
    st.button("Ver más", type="primary")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")
    st.button("Ver más", type="primary")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
    st.button("Ver más", type="primary")





st.write ("Hola mundo")
enable = st.checkbox("Enable camera")
picture = st.camera_input("Take a picture", disabled=not enable)

if picture:
    st.image(picture)





