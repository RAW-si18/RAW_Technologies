# Updated 23/1/24

import os
import time
import webbrowser as web
import datetime
from re import fullmatch
from typing import List
import pyperclip
import pyautogui as pg
import keyboard
import csv
from typing import Union
from raw_modules.speak_func import speak
from raw_modules.whats_core import *
from raw_modules.whats_exceptions import *
from raw_modules.whats_log import *
pg.FAILSAFE = False

check_connection()

def sendwhatmsg_instantly(
        phone_no: str,
        message: str,
        wait_time: int = 10,
        tab_close: bool = True,
        close_time: int = 2,
) -> None:
    """Send WhatsApp Message Instantly"""
    if not check_number(number=phone_no):
        speak("Sorry sir but Country Code Missing in Phone Number!")
        raise CountryCodeException("Country Code Missing in Phone Number!")
    phone_no = phone_no.replace(" ", "")
    if not fullmatch(r"^\+?[0-9]{2,4}\s?[0-9]{9,15}", phone_no):
        speak("Invalid Phone Number.")
        raise InvalidPhoneNumber("Invalid Phone Number.")
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
    log_message(receiver=phone_no, message=message)
    if tab_close:
        close_tab_website(wait_time=close_time)

def sending_or_video_immediately(
        phone_no: str,
        path: str,
        wait_time: int = 15,
        tab_close: bool = True,
        close_time: int = 3,
) -> None:
    """Send WhatsApp Message Instantly"""
    if not check_number(number=phone_no):
        speak("Country Code Missing in Phone Number!")
        raise CountryCodeException("Country Code Missing in Phone Number!")
    phone_no = phone_no.replace(" ", "")
    if not fullmatch(r"^\+?[0-9]{2,4}\s?[0-9]{9,15}", phone_no):
        speak("Invalid Phone Number.")
        raise InvalidPhoneNumber("Invalid Phone Number.")
    web.open(f"https://web.whatsapp.com/send?phone={phone_no}")
    time.sleep(wait_time)
    find_link()
    time.sleep(1)
    find_photo_or_video()
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
        close_tab_website(wait_time=close_time)

def sendwhatdoc_immediately(
        phone_no: str,
        path: str,
        wait_time: int = 15,
        tab_close: bool = True,
        close_time: int = 3,
) -> None:
    """Send WhatsApp Message Instantly"""
    if not check_number(number=phone_no):
        speak("Country Code Missing in Phone Number!")
        raise CountryCodeException("Country Code Missing in Phone Number!")
    phone_no = phone_no.replace(" ", "")
    if not fullmatch(r"^\+?[0-9]{2,4}\s?[0-9]{9,15}", phone_no):
        speak("Invalid Phone Number.")
        raise InvalidPhoneNumber("Invalid Phone Number.")
    web.open(f"https://web.whatsapp.com/send?phone={phone_no}")
    time.sleep(wait_time)
    find_link()
    time.sleep(1)
    find_document()
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
        close_tab_website(wait_time=close_time)

def sendwhatmsg(
        phone_no: str,
        message: Union[list, str],
        time_hour: int,
        time_min: int,
        wait_time: int = 15,
        tab_close: bool = True,
        close_time: int = 3,
) -> None:
    """Send a WhatsApp Message at a Certain Time"""
    if not check_number(phone_no):
        raise ValueError("Invalid Phone Number!")
    phone_no = phone_no.replace(" ", "")
    if not fullmatch(r'^\+?[0-9]{2,4}\s?[0-9]{9,15}', phone_no):
        raise ValueError("Invalid Phone Number.")
    now = datetime.datetime.now()
    current_hour = now.hour
    current_minute = now.minute
    time_diff_minutes = (time_hour * 60 + time_min) - (current_hour * 60 + current_minute)
    if time_diff_minutes < 0:
        time_diff_minutes += 24 * 60
    seconds_diff = time_diff_minutes * 60
    total_wait_time = seconds_diff - wait_time
    if total_wait_time <= 0:
        print("Time exceeded")
        return
    else:
        print(f"In {total_wait_time-30} seconds WhatsApp will open.")
        time.sleep(total_wait_time-30)
    if isinstance(message, list):
        send_message_list(message=message, receiver=phone_no, wait_time=wait_time)
    else:
        send_message(message=message, receiver=phone_no, wait_time=wait_time)
        log_message(receiver=phone_no, message=message)
    speak("WhatsApp message sent successfully.")
    if tab_close:
        close_tab_website(wait_time=close_time)

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
    now = datetime.datetime.now()
    current_hour = now.hour
    current_minute = now.minute
    if time_hour < current_hour or (time_hour == current_hour and time_min <= current_minute):
        time_hour += 24
    hours_diff = time_hour - current_hour
    minutes_diff = time_min - current_minute
    if minutes_diff < 0:
        hours_diff -= 1
        minutes_diff += 60
    seconds_diff = hours_diff * 3600 + minutes_diff * 60
    total_wait_time = seconds_diff - wait_time
    if total_wait_time <= 0:
        speak("Time exceeded")
        print("Wait time exceeds or equals total time to wait!")
    print(f"In {total_wait_time-30} Seconds WhatsApp will open.")
    speak(f"In {total_wait_time-30} Seconds WhatsApp will open.")
    send_message(message=message, receiver=group_id, wait_time=wait_time)
    log_message(receiver=group_id, message=message)
    speak("Message sent successfully.")
    if tab_close:
        close_tab_website(wait_time=close_time)

def sendwhatmsg_to_group_instantly(
        group_id: str,
        message: str,
        wait_time: int = 15,
        tab_close: bool = False,
        close_time: int = 3,
) -> None:
    """Send WhatsApp Message to a Group Instantly"""
    time.sleep(4)
    send_message(message=message, receiver=group_id, wait_time=wait_time)
    log_message(receiver=group_id, message=message)
    if tab_close:
        close_tab_website(wait_time=close_time)

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
    if (not receiver.isalnum()) and (not check_number(number=receiver)):
        raise CountryCodeException("Country Code Missing in Phone Number!")
    now = datetime.datetime.now()
    current_hour = now.hour
    current_minute = now.minute
    if time_hour < current_hour or (time_hour == current_hour and time_min <= current_minute):
        time_hour += 24
    hours_diff = time_hour - current_hour
    minutes_diff = time_min - current_minute
    if minutes_diff < 0:
        hours_diff -= 1
        minutes_diff += 60
    seconds_diff = hours_diff * 3600 + minutes_diff * 60
    total_wait_time = seconds_diff - wait_time
    if total_wait_time <= 0:
        speak("Time exceeded")
        print("Wait time exceeds or equals total time to wait!")
    print(f"In {total_wait_time-30} Seconds WhatsApp will open.")
    speak(f"In {total_wait_time-30} Seconds WhatsApp will open.")
    send_image(path=img_path, caption=caption, receiver=receiver, wait_time=wait_time)
    log_image(path=img_path, receiver=receiver, caption=caption)
    if tab_close:
        close_tab_website(wait_time=close_time)

def open_web() -> bool:
    """Opens WhatsApp Web"""
    try:
        web.open("https://web.whatsapp.com")
    except web.Error:
        return False
    else:
        return True
