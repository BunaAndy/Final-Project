import librosa
import numpy as np
import matplotlib.pyplot as plt
import wave, sys

file = wave.open("testAudio/C-Chord.wav")

signal = file.readframes(-1)
signal = np.frombuffer(signal)
librosa.display.waveshow(signal)

# def plot_magnitude_spectrum(signal, sr, title, f_ratio=1):
#     X = np.fft.fft(signal)
#     X_mag = np.absolute(X)
#     plt.figure(figsize=(18, 5))
#     f = np.linspace(0, sr, len(X_mag))
#     f_bins = int(len(X_mag)*f_ratio) 
#     plt.plot(f[:f_bins], X_mag[:f_bins])
#     plt.xlabel("Frequency (Hz)")
#     plt.title(title)

# plot_magnitude_spectrum(signal, 44100, "C Chord")