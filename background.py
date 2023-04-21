import time
import speech_recognition as sr


def callback(recognizer, audio):
    try:
        print(recognizer.recognize_sphinx(audio, language='es-MX'))
    except sr.UnknownValueError:
        print("Sphinx no ha podido reconocer el audio")
    except sr.RequestError as e:
        print("Ha ocurrido un error; {0}".format(e))


r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)


print('Escuchando...')
stop_listening = r.listen_in_background(m, callback)

for _ in range(5000):
    time.sleep(1)

print('fin')

stop_listening(wait_for_stop=False)
time.sleep(5)
