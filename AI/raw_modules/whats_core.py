# Updated 22/1/24 (UPDATE REQUIRED)

import os
import pathlib
import time
from platform import system
from urllib.parse import quote
from webbrowser import open
import requests
from raw_modules.speak_func import speak
from pyautogui import click, hotkey, locateOnScreen, moveTo, press, size, typewrite
from raw_modules.whats_exceptions import InternetException

WIDTH, HEIGHT = size()

def check_number(number: str) -> bool:
    '''returns bool whether True or False'''
    return "+" in number or "_" in number

def close_tab_website(wait_time: int = 2) -> None:
    '''close tab according to the os system'''
    time.sleep(wait_time)
    _system = system().lower() # Returns 'Windows', 'Linux', 'Darwin' (macOS), etc.
    if _system in ("windows", "linux"):
        hotkey("ctrl", "w")
    elif _system == "darwin":
        hotkey("command", "w")
    else:
        raise Warning(f"{_system} not supported!")
    press("enter")

def findtextbox() -> None:
    '''click on text bar on screen (Dependent on updates by whatsapp)'''
    try:
        location = locateOnScreen(r"H:\AI\resource_files\whatsapp_automation\color_smile.png")
        moveTo(location[0] + 230, location[1] + location[3]/2)
        click()
    except Exception:
        try:
            location = locateOnScreen(r"H:\AI\resource_files\whatsapp_automation\dark_smile.png")
            moveTo(location[0] + 230, location[1] + location[3]/2)
            click()        
        except Exception:
            try:
                location = locateOnScreen(r"H:\AI\resource_files\whatsapp_automation\light_smile.png")
                moveTo(location[0] + 230, location[1] + location[3]/2)
                click()
            except Exception:
                return

def find_link():
    '''click on link button on screen (Dependent on updates by whatsapp)'''
    try:
        location = locateOnScreen(r"H:\AI\resource_files\whatsapp_automation\color_link.png")
        moveTo(location[0] + 230, location[1] + location[3]/2)
        click()
    except Exception:
        try:
            location = locateOnScreen(r"H:\AI\resource_files\whatsapp_automation\dark_link.png")
            moveTo(location[0] + 230, location[1] + location[3]/2)
            click()        
        except Exception:
            try:
                location = locateOnScreen(r"H:\AI\resource_files\whatsapp_automation\light_link.png")
                moveTo(location[0] + 230, location[1] + location[3]/2)
                click()
            except Exception:
                return

def find_document():
    '''click on document button on screen (Dependent on updates by whatsapp)'''
    try:
        location = locateOnScreen(r"H:\AI\resource_files\whatsapp_automation\color_document.png")
        moveTo(location[0] + 230, location[1] + location[3]/2)
        click()
    except Exception:
        try:
            location = locateOnScreen(r"H:\AI\resource_files\whatsapp_automation\dark_document.png")
            moveTo(location[0] + 230, location[1] + location[3]/2)
            click()        
        except Exception:
            try:
                location = locateOnScreen(r"H:\AI\resource_files\whatsapp_automation\light_document.png")
                moveTo(location[0] + 230, location[1] + location[3]/2)
                click()
            except Exception:
                return

def find_photo_or_video():
    '''click on gallery button on screen (Dependent on updates by whatsapp)'''
    try:
        location = locateOnScreen(r"H:\AI\resource_files\whatsapp_automation\color_gallery.png")
        moveTo(location[0] + 230, location[1] + location[3]/2)
        click()
    except Exception:
        try:
            location = locateOnScreen(r"H:\AI\resource_files\whatsapp_automation\dark_gallery.png")
            moveTo(location[0] + 230, location[1] + location[3]/2)
            click()        
        except Exception:
            try:
                location = locateOnScreen(r"H:\AI\resource_files\whatsapp_automation\light_gallery.png")
                moveTo(location[0] + 230, location[1] + location[3]/2)
                click()
            except Exception:
                return

def check_connection() -> None:
    '''checking internet connection'''
    try:
        requests.get("https://google.com", timeout=5)
    except requests.RequestException:
        speak("Sorry sir, disruption in internet connection")
        raise InternetException("Error while connecting to the Internet. Make sure you are connected to the Internet!")

def _web(receiver: str, message: str) -> None:
    '''search for the receiver'''
    if check_number(number=receiver):
        open(
            "https://web.whatsapp.com/send?phone="
            + receiver
            + "&text="
            + quote(message)
        )
    else:
        open("https://web.whatsapp.com/accept?code=" + receiver)

def send_message(message: str, receiver: str, wait_time: int) -> None:
    '''sending message on whatsapp'''
    _web(receiver=receiver, message=message)
    time.sleep(7)
    findtextbox()
    time.sleep(wait_time - 7)
    if not check_number(number=receiver):
        index = 0
        length = len(message)
        while index < length:
            letter = message[index]
            if letter == ":":    
                typewrite(letter)
                index += 1
                while index < length:
                    letter = message[index]
                    if letter == ":":
                        press("enter")
                        break
                    typewrite(letter)
                    index += 1
            elif letter == "\n":
                hotkey("shift", "enter")
            else:
                typewrite(letter)
            index += 1
    time.sleep(2)
    press("enter")


def send_message_list(message: list, receiver: str, wait_time: int) -> None:
    '''send messages'''
    _web(receiver=receiver, message='')
    time.sleep(7)
    findtextbox()
    time.sleep(wait_time - 7)
    for msg in message:
        typewrite(msg)
        time.sleep(2)
        press("enter")

def copy_image(path: str) -> None:
    '''copy image'''
    _system = system().lower()
    if _system == "linux":
        if pathlib.Path(path).suffix in (".PNG", ".png"):
            os.system(f"copyq copy image/png - < {path}")
        elif pathlib.Path(path).suffix in (".jpg", ".JPG", ".jpeg", ".JPEG"):
            os.system(f"copyq copy image/jpeg - < {path}")
        else:
            speak(f"File Format {pathlib.Path(path).suffix} is not Supported!")
            raise Exception(f"File Format {pathlib.Path(path).suffix} is not Supported!")
    elif _system == "windows":
        from io import BytesIO
        import win32clipboard
        from PIL import Image
        image = Image.open(path)
        output = BytesIO()
        image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.close()
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()
    elif _system == "darwin":
        if pathlib.Path(path).suffix in (".jpg", ".jpeg", ".JPG", ".JPEG"):
            os.system(f"osascript -e 'set the clipboard to (read (POSIX file \"{path}\") as JPEG picture)'")
        else:
            raise Exception(
                f"File Format {pathlib.Path(path).suffix} is not Supported!"
            )
    else:
        raise Exception(f"Unsupported System: {_system}")

def send_image(path: str, caption: str, receiver: str, wait_time: int) -> None:
    '''send image'''
    _web(message=caption, receiver=receiver)
    time.sleep(7)
    findtextbox()
    time.sleep(wait_time - 7)
    copy_image(path=path)
    if not check_number(number=receiver):
        for char in caption:
            if char == "\n":
                hotkey("shift", "enter")
            else:
                typewrite(char)
    else:
        typewrite(" ")
    if system().lower() == "darwin":
        hotkey("command", "v")
    else:
        hotkey("ctrl", "v")
    time.sleep(1)
    findtextbox()
    press("enter")
