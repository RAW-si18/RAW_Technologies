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

# returns bool whether True or False
def check_number(number: str) -> bool:
    return "+" in number or "_" in number

# close tab according to the os system
def close_tab_website(wait_time: int = 2) -> None:
    time.sleep(wait_time)
    _system = system().lower() # Returns 'Windows', 'Linux', 'Darwin' (macOS), etc.
    if _system in ("windows", "linux"):
        hotkey("ctrl", "w")
    elif _system == "darwin":
        hotkey("command", "w")
    else:
        raise Warning(f"{_system} not supported!")
    press("enter")

# click on text bar on screen (Dependent on updates by whatsapp)
def findtextbox() -> None:
    location = locateOnScreen(r"H:\AI\resource_files\whatsapp_automation\color_smile.png")
    try:
        moveTo(location[0] + 230, location[1] + location[3]/2)
        click()
    except Exception:
        try:
            location = locateOnScreen(r"H:\AI\resource_files\whatsapp_automation\dark_smile.png")
            moveTo(location[0] + 230, location[1] + location[3]/2)
            click()        
        except Exception:
            location = locateOnScreen(r"H:\AI\resource_files\whatsapp_automation\light_smile.png")
            moveTo(location[0] + 230, location[1] + location[3]/2)
            click()

# click on link button on screen (Dependent on updates by whatsapp)
def find_link():
    location = locateOnScreen(r"H:\AI\resource_files\whatsapp_automation\color_link.png")
    try:
        moveTo(location[0] + 230, location[1] + location[3]/2)
        click()
    except Exception:
        try:
            location = locateOnScreen(r"H:\AI\resource_files\whatsapp_automation\dark_link.png")
            moveTo(location[0] + 230, location[1] + location[3]/2)
            click()        
        except Exception:
            location = locateOnScreen(r"H:\AI\resource_files\whatsapp_automation\light_link.png")
            moveTo(location[0] + 230, location[1] + location[3]/2)
            click()

# click on document button on screen (Dependent on updates by whatsapp)
def find_document():
    location = locateOnScreen(r"H:\AI\resource_files\whatsapp_automation\color_document.png")
    try:
        moveTo(location[0] + 230, location[1] + location[3]/2)
        click()
    except Exception:
        try:
            location = locateOnScreen(r"H:\AI\resource_files\whatsapp_automation\dark_document.png")
            moveTo(location[0] + 230, location[1] + location[3]/2)
            click()        
        except Exception:
            location = locateOnScreen(r"H:\AI\resource_files\whatsapp_automation\light_document.png")
            moveTo(location[0] + 230, location[1] + location[3]/2)
            click()

# click on gallery button on screen (Dependent on updates by whatsapp)
def find_photo_or_video():
    location = locateOnScreen(r"H:\AI\resource_files\whatsapp_automation\color_gallery.png")
    try:
        moveTo(location[0] + 230, location[1] + location[3]/2)
        click()
    except Exception:
        try:
            location = locateOnScreen(r"H:\AI\resource_files\whatsapp_automation\dark_gallery.png")
            moveTo(location[0] + 230, location[1] + location[3]/2)
            click()        
        except Exception:
            location = locateOnScreen(r"H:\AI\resource_files\whatsapp_automation\light_gallery.png")
            moveTo(location[0] + 230, location[1] + location[3]/2)
            click()

# checking internet connection
def check_connection() -> None:
    try:
        requests.get("https://google.com", timeout=5)
    except requests.RequestException:
        speak("Sorry sir, disruption in internet connection")
        raise InternetException("Error while connecting to the Internet. Make sure you are connected to the Internet!")

# search for the receiver
def _web(receiver: str, message: str) -> None:
    if check_number(number=receiver):
        open(
            "https://web.whatsapp.com/send?phone="
            + receiver
            + "&text="
            + quote(message)
        )
    else:
        open("https://web.whatsapp.com/accept?code=" + receiver)

# sending message on whatsapp
def send_message(message: str, receiver: str, wait_time: int) -> None:
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
    findtextbox()
    time.sleep(2)
    press("enter")

# send messages
def send_message_list(message: list, receiver: str, wait_time: int) -> None:
    _web(receiver=receiver, message='')
    time.sleep(7)
    findtextbox()
    time.sleep(wait_time - 7)
    for msg in message:
        typewrite(msg)
        time.sleep(2)
        press("enter")

# copy image
def copy_image(path: str) -> None:
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

# send image
def send_image(path: str, caption: str, receiver: str, wait_time: int) -> None:
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
