from pocketsphinx import LiveSpeech
import speech_recognition as sr
import os
from time import sleep

speech = LiveSpeech(lm=False, keyphrase='adam', kws_threshold=1e-5)
r = sr.Recognizer()

print('Esperando peticiones...')


def speak(text):
    os.system(f"espeak '{text}' -ves-la")


for phrase in speech:
    out = phrase.segments(detailed=False)

    if out[0] == 'adam':
        print('Nombre detectado!')
        speak('si senior, lo escucho')

        with sr.Microphone() as source:
            print('Escuchando comando...')
            audio = r.listen(source)

        speak('Procesando audio...')

        try:
            rtext = r.recognize_sphinx(audio, language='es-MX')
            print('palabras reconocidas >>>', rtext)
            speak(rtext)
        except sr.UnknownValueError:
            print('Sphinx no ha podido reconocer el audio')
        except sr.RequestError as e:
            print('Error de sphinx >>>', e)

        print('-'*20)
