from cgitb import text
from email.mime import audio
from gtts import gTTS
from playsound import playsound
from tkinter import *

text = input("Podaj tekst, który ma być przerobiony na audio: ")
print("Tekst został przerobiony.")
audio = 'audio.mp3'
language = "pl"
sp = gTTS(text=text, lang = language, slow=False)
sp.save(audio)

