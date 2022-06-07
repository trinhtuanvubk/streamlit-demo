import streamlit as st 
from time import sleep
from aiortc.contrib.media import MediaRecorder

results = st.button('start record')
st.write(results)
if results == True:
    results = False
    player = MediaRecorder('./ok.wav')
    player.start()
    sleep(2)
    player.stop()