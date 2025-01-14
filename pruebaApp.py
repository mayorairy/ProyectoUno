import streamlit as st
st.write ("Hola mundo")

enable = st.checkbox("Activar camera")

import time

ph = st.empty()
N = 1*60
for secs in range(N,0,-1):
    mm, ss = secs//60, secs%60
    ph.metric("Countdown", f"{mm:02d}:{ss:02d}")
    time.sleep(1)
    
picture = st.camera_input("Take a picture", disabled=not enable)

if enable:
    picture = st.camera_input("Toma una foto")
    if picture:
        st.image(picture)




