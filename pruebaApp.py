import streamlit as st
import time

st.write ("Hola mundo")
enable = st.checkbox("Enable camera")
picture = st.camera_input("Take a picture", disabled=not enable)

if picture:
    st.image(picture)

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>




