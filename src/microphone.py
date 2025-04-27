import os
import time

import speech_recognition as sr
import torch
from faster_whisper import WhisperModel

MODEL = "small.en"
model = WhisperModel(MODEL, device="cpu", compute_type="int8")
pipeline = model.transcribe

r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    print("SIIIIIILLLLEENNCE")
    r.adjust_for_ambient_noise(source)

def recognize():
    with m as source:
        audio = r.listen(source)

    with open("audio.wav", "wb") as f:
        f.write(audio.get_wav_data())

    t = time.perf_counter()
    with torch.inference_mode():
        segments, info = pipeline("audio.wav", vad_filter=True)

    recognized = ""
    for segment in segments:
        recognized += segment.text

    os.remove("audio.wav")

    return recognized

