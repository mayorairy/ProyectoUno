import streamlit as st
import time

st.title("Bienvenido!")


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("¿Qúe es la discapacidad?")
    st.image("https://i.pinimg.com/736x/cf/66/33/cf66334166ddd4c120148dc07c492449.jpg")
    st.link_button("Ver más", "https://streamlit.io/gallery")


with col2:
    st.subheader("Academia de Lengua de Señas Mexicana")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLPDBoTi6oPkFB26U2bZSFX5xrVgxGI72FAw&s")
    st.link_button("Ver más", "https://streamlit.io/gallery")
    

with col3:
    st.subheader("Modelos y ayudas técnicas para la intervención")
    st.image("https://i.pinimg.com/736x/9d/3a/35/9d3a3531044579ff2381b7bcba1868fd.jpg")
    st.link_button("Ver más", "https://streamlit.io/gallery")

with col4:
    st.subheader("Un bilingüismo silencioso")
    st.image("https://i.pinimg.com/736x/9f/ce/c2/9fcec281834ca98e08f1587e8943e983.jpg")
    st.link_button("Ver más", "https://streamlit.io/gallery")

st.button("Comenzar a practicar LSM", type="primary")





enable = st.checkbox("Enable camera")
picture = st.camera_input("Take a picture", disabled=not enable)

if picture:
    st.image(picture)





