from frequency_array import get_freq_array
from tab_maker import make_tab

if __name__ == "__main__":

    path = "testAudio/LandslideSample.wav"
    print(make_tab(path, 9000))

    path = "testAudio/C-Travis.wav"
    print(make_tab(path, 44100))

    path = "testAudio/Guitar-C-Chord-Better.wav"
    print(make_tab(path, -1))
