import pathlib
import wave
from pydub import AudioSegment

DATASET_PATH = 'TestAudio/SingleNotes'

data_dir = pathlib.Path(DATASET_PATH)

for dir in data_dir.iterdir():
    for path in dir.iterdir():
        print(path)
        pathstr = str(path).replace("\\", "/")
        sound = AudioSegment.from_wav(pathstr)
        sound = sound.set_channels(1)
        sound.export("MonoAudio/" + pathstr, format="wav")

        # soundr = wave.open(pathstr)
        # soundw = wave.open("MonoAudio/" + pathstr, "w")
        # soundw.setnchannels(1)
        # soundw.writeframes(soundr)

