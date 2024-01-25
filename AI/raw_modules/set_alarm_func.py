# Updated 23/1/24

import time
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from raw_modules.calen_clock import clock
from raw_modules.similar_sent import cosine_sent
from raw_modules.speak_func import speak
import random
import keyboard

def set_alarm(hr: int, minu: int, ampm: str, purpose='reminder') -> None:
    '''alarm set up'''
    pygame.mixer.init()
    if hr > 12:
        speak("Oops! Are you sure that's a valid hour? Remember, it should be between 1 and 12.")
        print("Alarm setup failed")
        return
    if minu >= 60:
        speak("Whoa there! Are you telling me time travels faster than light? Minutes should be between 0 and 59.")
        print("Alarm setup failed")
        return
    if ampm.lower() == "pm" and hr != 12:
        hr += 12
    elif ampm.lower() == "am" and hr == 12:
        hr = 0
    alarm_seconds = hr * 3600 + minu * 60
    curr_hr, curr_min, curr_sec, curr_st = clock()
    curr_seconds = int(curr_hr) * 3600 + int(curr_min) * 60 + int(curr_sec)
    seconds = alarm_seconds - curr_seconds
    if seconds <= 0:
        speak("Uh-oh! It seems like time has slipped through our fingers. The alarm setup failed.")
        print("The alarm setup failed.")
        return
    speak(f"Alarm set for {seconds} seconds from now.")
    print(f"Alarm set for {seconds} seconds from now.")
    time.sleep(seconds)
    speak("Time's up!")
    print("Time's up! Alarm ringing...")
    speak(f"Alarm: {purpose}")
    print(f"Alarm: {purpose}")
    tune_type, matchper = cosine_sent(purpose, ["morning/wake up", "daily reminder", "work/class/urgent"])
    if tune_type == "morning/wake up":
        choice = random.randint(1, 3)
    elif tune_type == "daily reminder":
        choice = random.randint(2, 5)
    else:
        choice = random.randint(5, 7)
    paths = [
        "H:\\AI\\raw_cosmos\\resource_files\\morning.mp3",
        "H:\\AI\\raw_cosmos\\resource_files\\whistle.mp3",
        "H:\\AI\\raw_cosmos\\resource_files\\spiderman.mp3",
        "H:\\AI\\raw_cosmos\\resource_files\\suzume.mp3",
        "H:\\AI\\raw_cosmos\\resource_files\\wakanda.mp3",
        "H:\\AI\\raw_cosmos\\resource_files\\avenger.mp3",
        "H:\\AI\\raw_cosmos\\resource_files\\jarico.mp3"
    ]
    path_link = paths[choice - 1]
    pygame.mixer.music.load(path_link)
    pygame.mixer.music.set_volume(100)
    pygame.mixer.music.play()
    speak("Press space bar for stop")
    print("Press space bar for stop")
    while pygame.mixer.music.get_busy():
        if keyboard.is_pressed('space'): 
            pygame.mixer.music.stop()
            speak("Alarm stopped.")
            print("Alarm stopped")
            break
 