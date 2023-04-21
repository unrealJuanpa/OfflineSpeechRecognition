import speech_recognition as sr

r = sr.Recognizer()

input('Comenzar?')

with sr.Microphone() as source:
    print('Escuchando...')
    audio = r.listen(source)
print('Fin de escucha... Procesando audio')

try:
    rtext = r.recognize_sphinx(audio, language='es-MX')
    print('Sphinx thinks you said >>>', rtext)
except sr.UnknownValueError:
    print('Sphinx no ha podido reconocer el audio')
except sr.RequestError as e:
    print('Error de sphinx >>>', e)
