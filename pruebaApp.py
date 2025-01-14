import streamlit as st
import time

st.write ("Hola mundo")

enable = st.checkbox("Activar camera")

ph = st.empty()
for secs in range(10,0,-1):
    mm, ss = secs//60, secs%60
    ph.metric("Countdown", f"{mm:02d}:{ss:02d}")
    time.sleep(1)

if enable:
    picture = st.camera_input("Toma una foto")
    if picture:
        st.image(picture)




