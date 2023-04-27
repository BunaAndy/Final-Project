import matplotlib.pyplot as plt
import numpy as np
import wave, sys
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.io import wavfile # get the api
 
# shows the sound waves
def visualize(path: str):
   
    # reading the audio file
    raw = wave.open(path)
     
    # reads all the frames
    # -1 indicates all or max frames
    signal = raw.readframes(-1)
    signal = np.frombuffer(signal, dtype ="int16")
    

    # plt.plot(signal[:1000])
    # plt.show()
     
    # gets the frame rate
    sr = raw.getframerate()
 
    # to Plot the x-axis in seconds
    # you need get the frame rate
    # and divide by size of your signal
    # to create a Time Vector
    # spaced linearly with the size
    # of the audio file
    # time = np.linspace(
    #     0, # start
    #     1,
    #     num = len(signal)
    # )
 
    # using matplotlib to plot
    # creates a new figure
    # plt.figure(1)
     
    # title of the plot
    # plt.title("Sound Wave")
     
    # label of x-axis
    # plt.xlabel("Time")
    
    # actual plotting
    # plt.plot(time, signal)
     
    # # shows the plot
    # # in new window
    # plt.show()

    # Logistic regression using previous 3 and next 3 frames that had notes played as features. 0's are ignored. 1 is 0 in tablature
    # Only need to find out what string it is on, the frequency follows from there

     # load the data
    c = fft(signal) # you only need half of the fft list (real signal symmetry)
    freqs = np.fft.fftfreq(len(c))
    # print(freqs.min(), freqs.max())
    # print(freqs)
    idx = np.argmax(np.abs(c))
    # print(np.abs(c))
    signalabs = np.abs(c)

    sig_freqs = []
    for id, exp in enumerate(signalabs):
        if exp > 1000000000:
            sig_freqs.append(abs(freqs[id] * sr))
    
    print(sig_freqs)

    # print(signalabs[np.argmin(signalabs)])
    # print(signalabs[np.argmax(signalabs)])
    # freq = freqs[idx]
    # freq_in_hertz = abs(freq * sr)
    # print(freq_in_hertz)

    # print(c)
    # d = len(c)/2

    # N = sr * 10

    # yf = fft(signal)
    # xf = fftfreq(N, 1 / sr)
    # np.savetxt("foo.csv", np.abs(c), delimiter=",")

    # plt.plot(xf, np.abs(yf))
    # plt.xlim([0, 500])
    # plt.show()
    
    # plt.plot(abs(c[:]),'r')
    # plt.show()
 
    # you can also save
    # the plot using
    # plt.savefig('filename')