import streamlit as st 
from IPython.display import Audio
from ipywebrtc import CameraStream, AudioRecorder
from record import app
from helper import mapping_words

title = 'Hate Speech Detection'
st.title(title)

st.write('''## Voice Data Collection''')


dicts = mapping_words('list_words.txt')
words = set(dicts.keys())
sel_words = st.sidebar.selectbox('Select Word',words)
number = dicts[sel_words]



name = st.text_input('Enter your name','')

app(number=number,usr_name=name)

# path = app.
# st.audio(data ='example.wav',format= 'wav')













