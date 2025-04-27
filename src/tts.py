from kokoro import KPipeline
import soundfile as sf
from pydub import AudioSegment
from pydub.playback import play
import os

pipeline = KPipeline(lang_code='a')
FILE = "s.wav"

def speak(text):
    generator = pipeline(text, voice='af_heart')
    for i, (gs, ps, audio) in enumerate(generator):
        sf.write(FILE, audio, 24000)
        audio = AudioSegment.from_wav(FILE)
        play(audio)
        os.remove(FILE)
        break

