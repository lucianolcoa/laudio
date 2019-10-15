import pyaudio
import time
import numpy as np
from matplotlib import pyplot as plt
import scipy.signal as signal

from scipy.fftpack import rfft, irfft, fftfreq

CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()
#fulldata = np.array([])
#dry_data = np.array([])
mask=[]
novoarray=[]
def main():
    dados=open("dados.txt","r")
    dados=dados.read()
    
    print (dados)
    dados=dados.split(",")
    global filtrob 
    global filtroa
    global efeito
    global tempo
    filtrob=int(dados[1])
    filtroa=int(dados[2])
    efeito= int(dados[3])
    tempo= int(dados[0])
    global lista
    global novoarray
    l=0
    stream = p.open(format=pyaudio.paFloat32,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                input=True,
                stream_callback=callback)

    stream.start_stream()

    while stream.is_active():
        for i in range(1025):
            novoarray.append(0)
        
        time.sleep(tempo)
        stream.stop_stream()
        stream.close()

    #numpydata = np.hstack(fulldata)
    #plt.plot(numpydata)
    #plt.title("Wet")
    #plt.show()
    #numpydata = np.hstack(dry_data)
    #plt.plot(numpydata)
    #plt.title("Dry")
    #plt.show()
    #p.terminate()

def callback(in_data, frame_count, time_info, flag):
    global novoarray
    LOWPASS = filtrob # Hz
    SAMPLE_RATE = 44100 # Hz
    FFT_LENGTH = 2048
    OVERLAP = 512
    HIGHPASS = filtroa # Hz
    FFT_SAMPLE = FFT_LENGTH - OVERLAP
    NYQUIST_RATE = SAMPLE_RATE / 2.0
    LOWPASS /= (NYQUIST_RATE / (FFT_LENGTH / 2.0))
    HIGHPASS /= (NYQUIST_RATE / (FFT_LENGTH / 2.0))
    audio_data = np.fromstring(in_data, dtype=np.float32)
    
    novoarray1=np.asarray(novoarray)
    freq=fftfreq(1024)
     
    l=len(audio_data)
    ff=0
    fff=0
    for ff in range(0, 1024):
        rampdown = 1.0
        if ff > LOWPASS:
           rampdown = 0.0
        elif ff < HIGHPASS:
           rampdown = 0.0
           mask.append(rampdown)
           fff+=1
    ff=0
    
    print (len(mask))
    x=audio_data.astype(np.float32)
    y=rfft(x)
    print (y[512])
    #print (mask[len(mask)-1])
    for ff in range(fff):
        y[ff] *= mask[ff]
        
        ff+=1
    ff=0
  
    i=0
    
    yy = y.copy()
   
    yy[(freq<0.001)] = 0
    N=len(yy)
   
    shifted_freq = np.zeros(N, yy.dtype)
    #aqui se altera a voz e cria o efeito distorção
    shift=efeito
    
    S = np.round(shift if shift > 0 else N + shift, 0)
    s = N - S
    shifted_freq[:S] = yy[s:]
    shifted_freq[S:] = yy[:s]
    z=irfft(shifted_freq)
    
   
   
    print(yy)
    
    
    
    
    return (z, pyaudio.paContinue)

main()