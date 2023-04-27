import matplotlib.pyplot as plt
import numpy as np
import wave, sys
import matplotlib.pyplot as plt
from scipy.fft import fft

FREQLIST = [82,87,92,98,104,110,117,123,131,139,147,156,165,
            175,185,196,208,220,233,247,262,277,294,311,330,
            349,370,392,415,440,466,494,523,554,587,622,659]

def round_freq(bad_freq: float):
    closest = -100
    for freq in FREQLIST:
        if abs(bad_freq - closest) > abs(bad_freq - freq):
            closest = freq
    return closest

def get_frequencies(wave: wave.Wave_read, numFrames: int):
    # Read the specified number of frames in the Wave_read object
    signal = wave.readframes(numFrames)
    signal = np.frombuffer(signal, dtype ="int16")

    # Get framerate, used to calculate frequencies
    framerate = wave.getframerate()

    # Perform Fast Fourier on signal found
    fourierOut = fft(signal)
    # Get the frequencies found in cycles/frame
    freqs = np.fft.fftfreq(len(fourierOut))
    # Get all frequencies as absolute values, since negative frequences are the same as positive ones, just phase-shifted
    signalabs = np.abs(fourierOut)

    sig_freqs = []
    # for every entry in the frequencies found, return the exponents that are above 1000000000
    # The higher the number, the more the filter. A very noisy or distorted sound can still be read with this higher
    # value, but need more testing to find if a shorter framerate influences this
    for id, exp in enumerate(signalabs):
        if exp > 7000000:
            # Calculate the actual frequencies found by multiplying the cycles/frame by the framerate
            sig_freqs.append(round_freq(abs(freqs[id] * framerate)))

    # Return list of set of frequencies, essentially removng any duplicates found
    return list(set(sig_freqs))

# return a list of list of frequencies. Each list of frequencies is a single read
# of a section of music, ie eighth note, quarter note, etc. Based on number of frames in the found wav file
# Using -1 or anything above the total number of frames for frameSplit analyzes the entire wav file
def get_freq_array(filepath: str, frameSplit: int):
    raw = wave.open(filepath)
    splits = []
    if (frameSplit == -1):
        frameSplit = raw.getnframes() - 1
    for split in range(0, raw.getnframes(), frameSplit):
        raw.setpos(split)
        splits.append(get_frequencies(raw, frameSplit))
    return splits