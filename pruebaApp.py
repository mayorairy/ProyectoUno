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
#    picture = st.camera_input("Toma una foto")
#    if picture:
#        st.image(picture)

    img_file_buffer = st.camera_input("Take a picture", disabled= True)
    

    if img_file_buffer is not None:
        # To read image file buffer as bytes:
        bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
        st.write(type(bytes_data))




