# Updated 23/1/24 (UPDATE NOT REQUIRED)

import os
import time
import webbrowser as web
from datetime import datetime
from re import fullmatch
from typing import List
import pyperclip
import pyautogui as pg
import keyboard
import csv
from typing import Union
from raw_modules.speak_func import speak
from raw_modules.whats_core import core, exceptions, log

pg.FAILSAFE = False

core.check_connection()

def sendwhatmsg_instantly(
        phone_no: str,
        message: str,
        wait_time: int = 10,
        tab_close: bool = True,
        close_time: int = 2,
) -> None:
    """Send WhatsApp Message Instantly"""
    if not core.check_number(number=phone_no):
        speak("Sorry sir but Country Code Missing in Phone Number!")
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")
    phone_no = phone_no.replace(" ", "")
    if not fullmatch(r"^\+?[0-9]{2,4}\s?[0-9]{9,15}", phone_no):
        speak("Invalid Phone Number.")
        raise exceptions.InvalidPhoneNumber("Invalid Phone Number.")
    web.open(f"https://web.whatsapp.com/send?phone={phone_no}")
    time.sleep(wait_time)
    index = 0
    length = len(message)
    while index < length:
        letter = message[index]
        pg.write(letter)
        if letter == ":":
            index += 1
            while index < length:
                letter = message[index]
                if letter == ":":
                    pg.press("enter")
                    break
                pg.write(letter)
                index += 1
        index += 1
    time.sleep(2)
    pg.press("enter")
    speak("Whatsapp message sent successfully sir.")
    log.log_message(receiver=phone_no, message=message)
    if tab_close:
        core.close_tab(wait_time=close_time)

def sending_or_video_immediately(
        phone_no: str,
        path: str,
        wait_time: int = 15,
        tab_close: bool = True,
        close_time: int = 3,
) -> None:
    """Send WhatsApp Message Instantly"""
    if not core.check_number(number=phone_no):
        speak("Country Code Missing in Phone Number!")
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")
    phone_no = phone_no.replace(" ", "")
    if not fullmatch(r"^\+?[0-9]{2,4}\s?[0-9]{9,15}", phone_no):
        speak("Invalid Phone Number.")
        raise exceptions.InvalidPhoneNumber("Invalid Phone Number.")
    web.open(f"https://web.whatsapp.com/send?phone={phone_no}")
    time.sleep(wait_time)
    core.find_link()
    time.sleep(1)
    core.find_photo_or_video()
    pyperclip.copy(os.path.abspath(path))
    time.sleep(1)
    keyboard.press("ctrl")
    keyboard.press("v")
    keyboard.release("v")
    keyboard.release("ctrl")
    time.sleep(1)
    keyboard.press("enter")
    keyboard.release("enter")
    time.sleep(1)
    keyboard.press("enter")
    keyboard.release("enter")
    speak("Sent successfully sir.")
    if tab_close:
        core.close_tab(wait_time=close_time)

def sendwhatdoc_immediately(
        phone_no: str,
        path: str,
        wait_time: int = 15,
        tab_close: bool = True,
        close_time: int = 3,
) -> None:
    """Send WhatsApp Message Instantly"""
    if not core.check_number(number=phone_no):
        speak("Country Code Missing in Phone Number!")
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")
    phone_no = phone_no.replace(" ", "")
    if not fullmatch(r"^\+?[0-9]{2,4}\s?[0-9]{9,15}", phone_no):
        speak("Invalid Phone Number.")
        raise exceptions.InvalidPhoneNumber("Invalid Phone Number.")
    web.open(f"https://web.whatsapp.com/send?phone={phone_no}")
    time.sleep(wait_time)
    core.find_link()
    time.sleep(1)
    core.find_document()
    pyperclip.copy(os.path.abspath(path))
    time.sleep(1)
    keyboard.press("ctrl")
    keyboard.press("v")
    keyboard.release("v")
    keyboard.release("ctrl")
    time.sleep(1)
    keyboard.press("enter")
    keyboard.release("enter")
    time.sleep(1)
    keyboard.press("enter")
    keyboard.release("enter")
    speak("Document sent successfully.")
    if tab_close:
        core.close_tab(wait_time=close_time)

def sendwhatmsg(
        phone_no: str,
        message: Union[list, str],
        time_hour: int,
        time_min: int,
        wait_time: int = 15,
        tab_close: bool = False,
        close_time: int = 3,
) -> None:
    """Send a WhatsApp Message at a Certain Time"""
    if not core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")
    phone_no = phone_no.replace(" ", "")
    if not fullmatch(r'^\+?[0-9]{2,4}\s?[0-9]{9,15}', phone_no):
        raise exceptions.InvalidPhoneNumber("Invalid Phone Number.")
    if time_hour not in range(25) or time_min not in range(60):
        raise Warning("Invalid Time Format!")
    current_time = time.localtime()
    left_time = datetime.strptime(
        f"{time_hour}:{time_min}:0", "%H:%M:%S"
    ) - datetime.strptime(
        f"{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}",
        "%H:%M:%S",
    )
    if left_time.seconds < wait_time:
        raise exceptions.CallTimeException(
            "Call Time must be Greater than Wait Time as WhatsApp Web takes some Time to Load!"
        )
    sleep_time = left_time.seconds - wait_time
    print(
        f"In {sleep_time} Seconds WhatsApp will open."
    )
    time.sleep(sleep_time)
    if isinstance(message, list):
        core.send_message_list(message=message, receiver=phone_no, wait_time=wait_time)
    else:
        core.send_message(message=message, receiver=phone_no, wait_time=wait_time)
        log.log_message( receiver=phone_no, message=message)
    speak("Whatsapp message sent successfully.")
    if tab_close:
        core.close_tab(wait_time=close_time)

def show_history():
    '''shows whatsapp history'''
    with open(r"H:\AI\resource_files\whatsapp_history.csv", 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        length = sum(1 for _ in csv_reader)  # _ is just convention for variable not in use
        csv_file.seek(0) 
        header = next(csv_reader)
        if length == 0:
            speak("No data found!!")
            print("No data found!!")
            return
        print("Recent messages: ")
        for cursor, row in enumerate(csv_reader, start=1):
            if cursor <= length or cursor > length - 5:
                print("")
                print(f"DATE: {row[0]}/{row[1]}/{row[2]}")
                print(f"TIME: {row[3]}:{row[4]}:{row[5]}")
                print(f"RECEIVER ID/Ph_No: {row[6]} {row[7]}")
                print(f"MESSAGE: {row[8]}")

def sendwhatmsg_to_group(
        group_id: str,
        message: str,
        time_hour: int,
        time_min: int,
        wait_time: int = 15,
        tab_close: bool = False,
        close_time: int = 2,
) -> None:
    """Send WhatsApp Message to a Group at a Certain Time"""
    if time_hour not in range(25) or time_min not in range(60):
        speak("Invalid Time Format!")
        raise Warning("Invalid Time Format!")
    current_time = time.localtime()
    left_time = datetime.strptime(
        f"{time_hour}:{time_min}:0", "%H:%M:%S"
    ) - datetime.strptime(
        f"{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}",
        "%H:%M:%S",
    )
    if left_time.seconds < wait_time:
        raise exceptions.CallTimeException("Call Time must be Greater than Wait Time as WhatsApp Web takes some Time to Load!")
    sleep_time = left_time.seconds - wait_time
    speak(f"In {sleep_time} Seconds WhatsApp will open.")
    print(f"In {sleep_time} Seconds WhatsApp will open.")
    time.sleep(sleep_time)
    core.send_message(message=message, receiver=group_id, wait_time=wait_time)
    log.log_message(receiver=group_id, message=message)
    speak("Message sent successfully.")
    if tab_close:
        core.close_tab(wait_time=close_time)

def sendwhatmsg_to_group_instantly(
        group_id: str,
        message: str,
        wait_time: int = 15,
        tab_close: bool = False,
        close_time: int = 3,
) -> None:
    """Send WhatsApp Message to a Group Instantly"""
    time.sleep(4)
    core.send_message(message=message, receiver=group_id, wait_time=wait_time)
    log.log_message(receiver=group_id, message=message)
    if tab_close:
        core.close_tab(wait_time=close_time)

def sendwhatsmsg_to_all(
        phone_nos: List[str],
        message: str,
        time_hour: int,
        time_min: int,
        wait_time: int = 15,
        tab_close: bool = False,
        close_time: int = 3,
) -> None:
    '''send whatsapp message to all'''
    for phone_no in phone_nos:
        sendwhatmsg(phone_no, message, time_hour, time_min, wait_time, tab_close, close_time)

def sendwhats_image(
        receiver: str,
        img_path: str,
        time_hour: int,
        time_min: int,
        caption: str = "",
        wait_time: int = 15,
        tab_close: bool = False,
        close_time: int = 3,
) -> None:
    """Send Image to a WhatsApp Contact or Group at a Certain Time"""
    if (not receiver.isalnum()) and (not core.check_number(number=receiver)):
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")
    current_time = time.localtime()
    left_time = datetime.strptime(
        f"{time_hour}:{time_min}:0", "%H:%M:%S"
    ) - datetime.strptime(
        f"{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}",
        "%H:%M:%S",
    )
    if left_time.seconds < wait_time:
        raise exceptions.CallTimeException("Call Time must be Greater than Wait Time as WhatsApp Web takes some Time to Load!")
    sleep_time = left_time.seconds - wait_time
    print(f"In {sleep_time} Seconds WhatsApp will open.")
    time.sleep(sleep_time)
    core.send_image(path=img_path, caption=caption, receiver=receiver, wait_time=wait_time)
    log.log_image(_time=current_time, path=img_path, receiver=receiver, caption=caption)
    if tab_close:
        core.close_tab(wait_time=close_time)

def open_web() -> bool:
    """Opens WhatsApp Web"""
    try:
        web.open("https://web.whatsapp.com")
    except web.Error:
        return False
    else:
        return True
