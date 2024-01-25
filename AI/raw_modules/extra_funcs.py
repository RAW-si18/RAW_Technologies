# Web browser with url
import webbrowser
from raw_modules.speak_func import speak

def webopen(url: str) -> None:
    '''open website with particular url'''
    webbrowser.open(url)
    speak("Opening website.")
    print('Opening website')