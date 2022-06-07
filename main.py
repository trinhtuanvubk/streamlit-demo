import streamlit as st 
from IPython.display import Audio
from ipywebrtc import CameraStream, AudioRecorder
from record import app
from helper import mapping_words
import numpy as np 

# titile 
title = 'Hate Speech Detection'
st.title(title)
st.write('''## Voice Data Collection''')

# each words with a number 
dicts = mapping_words('list_words.txt')
print(dicts)
print("ok")
# get all words 
words = np.asarray((list(dicts.keys())))
print("done")
# the word that user choose 
sel_words = st.sidebar.selectbox('Select Word',words)
# number of the word 
number = dicts[sel_words]
# text box to enter the name 
name = st.text_input('Enter your name','')

st.write(f'Hi {name}, please click start then say the word you chose')

app(number=number,usr_name=name)














