import os
import matplotlib.pyplot as plt
import numpy as np 
from scipy.io import wavfile

# create a function to map each words with a number 
def mapping_words(list_path): 
    with open(list_path,'r') as f_in : 
        lines = f_in.readlines()
        dicts = {}
        for count,l in enumerate(lines) : 
            dicts[l.strip()] = count
            if not os.path.isdir('./data/' + str(count)):
                os.mkdir('./data/'+ str(count))
    f_in.close()
    return dicts

#  create a function to draw spectrogram 
def draw_spectrogram(file_path) : 
    # Read the wav file 
    samplingFrequency, signalData = wavfile.read(file_path)
    # Plot the signal read from wav file
    plt.title('Spectrogram of your wav file')
    plt.plot(signalData)
    plt.xlabel('Sample')
    plt.ylabel('Amplitude')
    plt.specgram(signalData,Fs=samplingFrequency)



            
    



