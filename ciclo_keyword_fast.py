from pocketsphinx import LiveSpeech
import speech_recognition as sr
import os
from time import sleep

speech = LiveSpeech(lm=False, kws='key.list', dic='key.dict')
r = sr.Recognizer()

print('Esperando peticiones...')


def speak(text):
    os.system(f"espeak '{text}' -ves-la")


for phrase in speech:
    out = phrase.segments(detailed=False)
    print(out)
