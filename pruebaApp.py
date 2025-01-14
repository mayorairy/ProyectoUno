import streamlit as st
import time
st.write ("Hola mundo")

enable = st.checkbox("Activar camera")

def count_down(ts):
    while ts:
        mins, secs = divmod (ts,60)
        time_now='{:02d}:{:02d}'.format(mins,secs)
    print(f"{time_now}")
    time.sleep(1)
    ts -= 1

picture = st.camera_input("Take a picture", disabled=not enable)

if picture:
    st.image(picture)




