from pocketsphinx import LiveSpeech

print('inicio ciclo for...')
for phrase in LiveSpeech():
    print(phrase)
