from pocketsphinx import LiveSpeech
import os

speech = LiveSpeech(lm=False, keyphrase='adam', kws_threshold=1e-8)

print('inicio ciclo for.')
for phrase in speech:
    out = phrase.segments(detailed=True)

    print(out)

    if out[0] == 'adam':
        os.system("espeak 'si senior, lo escucho' -ves-la")
