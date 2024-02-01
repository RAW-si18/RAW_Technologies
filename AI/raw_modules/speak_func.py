# Updated 23/1/24

import pyttsx3
hfbot=pyttsx3.init('sapi5')
voices=hfbot.getProperty('voices') # voice taken
hfbot.setProperty('rate', 180) #rate of speak3
rate=hfbot.getProperty('rate')
hfbot.setProperty('voice', voices[0].id)

def speak(audio: str) -> None:
    hfbot.say(audio)
    hfbot.runAndWait()
