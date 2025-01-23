import streamlit as st
import time

def pagina_principal():
    container = st.container(border=True)   
    container.write("Home")
    container.title("Bienvenido!")
    container.write("Usa le menú de la izquierda para navegar entre las páginas!")
    
 
    container.col1, container.col2, container.col3, container.col4 = st.columns(4)
        
    with container.col1:
        st.subheader("¿Qúe es la discapacidad?")
        st.image("https://i.pinimg.com/736x/cf/66/33/cf66334166ddd4c120148dc07c492449.jpg")
        st.link_button("Ver más", "https://streamlit.io/gallery")
        
        
    with container.col2:
        st.subheader("Academia de Lengua de Señas Mexicana")
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLPDBoTi6oPkFB26U2bZSFX5xrVgxGI72FAw&s")
        st.link_button("Ver más", "https://streamlit.io/gallery")
            
        
    with container.col3:
        st.subheader("Modelos y ayudas técnicas para la intervención")
        st.image("https://i.pinimg.com/736x/9d/3a/35/9d3a3531044579ff2381b7bcba1868fd.jpg")
        st.link_button("Ver más", "https://streamlit.io/gallery")
        
    with container.col4:
        st.subheader("Un bilingüismo silencioso")
        st.image("https://i.pinimg.com/736x/9f/ce/c2/9fcec281834ca98e08f1587e8943e983.jpg")
        st.link_button("Ver más", "https://streamlit.io/gallery")
        
    container.button("Comenzar a practicar LSM", type="primary")

def practicar_lsm():
    container = st.container(border=True)   
    container.title("Abecedario")
    container.write("Practicar LSM")
    container.write("Activa la camara para comenzar a practicar")
    enable = st.checkbox("Enable camera")
    picture = st.camera_input("Take a picture", disabled=not enable)

    if picture:
        st.image(picture)
    

st.sidebar.title("Navegación")
pagina = st.sidebar.selectbox("Selecciona una página",["Principal", "Buscar", "Perfil", "Practicar", "Contacto"])

if pagina == "Principal":
    pagina_principal() 

elif pagina == "Practicar":
    practicar_lsm()









