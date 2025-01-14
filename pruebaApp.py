import streamlit as st
st.write ("Hola mundo")

enable = st.checkbox("Activar camera")
picture = st.camera_input("Tomar foto", disabled=not enable)

if picture:
    st.image(picture)

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
    st.write(type(bytes_data))

import time 
def count_down(ts)
    while ts:
        mins, secs = divmod (ts,60)
        time_now= '{:02d}:
'{:02d}:.format(mins,secs)
    print(f"{time_now}")
    time.sleep(1)
    ts -= 1
