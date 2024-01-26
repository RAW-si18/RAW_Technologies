# Updated 26/1/24

from raw_modules.spttxt import commandeng
from raw_modules.speak_func import speak
from raw_modules.raw_messenger import send_whatsapp_msg, send_whatsapp_image, send_whatsapp_msg_toall
from raw_modules.raw_messenger import show_history_msg, take_screenshot_pc
from raw_modules.similar_sent import cosine_sent
from raw_modules.contacts import get_all_aliases
from raw_modules.calen_clock import clock
from raw_modules.similar_word import match_word_func
from raw_modules.ascii_art import image_to_ascii_art
from typing import Optional
import threading

def func_for_set5_1() -> Optional[str]:
    '''helping function for whatsapp alias name'''
    all_alias=get_all_aliases()
    if all_alias is None:
        return None
    speak("Speak out the name whom you want to send whatsapp message.")
    alias_name=commandeng()
    if alias_name=='None':
        return None
    alias_name_list=match_word_func(alias_name,all_alias)
    if not alias_name_list:
        speak("Sorry sir something went wrong.")
        print("Sorry sir something went wrong.")
        speak("Enter alias name.")
        alias_name=input("Enter alias name: ")
        alias_name_list=match_word_func(alias_name,all_alias)
        if not alias_name_list:
            speak("No such alias name found.")
            print("No such alias name found.")
            return None
    if len(alias_name_list)==1:
        alias_name=alias_name_list[0]
    else:
        alias_name,_=cosine_sent(alias_name,alias_name_list)
        speak(f"Is this whatsapp Message schedule for {alias_name}. Yes or no.")
        ch=commandeng()
        if ch=="None":
            speak("Defaulting to yes.")
            ch='yes'
        elif "no" in ch:
            ch='no'
            speak("I apologize, sir, but I am having difficulty determining the correct alias name.\nCould you please inform me which one of the following options is the closest match?\nIf none of the options matches, kindly specify 'none'.")
            j=1
            for i in alias_name_list:
                print(f"alias {j}: {i}")
                j+=1
            print(f"Please enter {j} if none of the above options align with your preference.")
            speak(f"Please enter {j} if none of the above options align with your preference.")
            alias_name_list.append("none")
            check=int(input("Enter the option number for your desired alias: "))
            if check>j:
                speak(f"Oops! Looks like you took a detour to the land of invalid inputs. Only choices 1 to {j} are invited to the party!")
                print("Query dismissed")
                return None
            alias_name=alias_name_list[check-1]
            if alias_name=="none":
                speak("Apologies, sir. I couldn't determine the alias name. We're terminating this query.\nPlease double-check the alias name.")
                return None
    return alias_name
        
def ch30_func(cmd: str) -> None:
    '''whatsapp message'''
    speak("Triggering WhatsApp Message sequel.")
    print('Raw whatsapp messenger')
    alias_name=func_for_set5_1()
    if alias_name==None:
        return
    speak("At what time do you want to send message.")
    if "now" in cmd:
        hr, mint, sec, ampm = clock()
        if sec<30:
            mint+=1
        else:
            mint+=2
        if mint >= 60:
            mint -= 60
            hr += 1
            if hr > 12:
                hr -= 12
                ampm = 'pm' if ampm == 'am' else 'am'
    else:
        hr=int(input("Enter hour (12 hour format): "))
        if (hr>12) or (hr<1):
            speak("Invalid input entered sir. Terminating query.")
            print("Invalid hour")
            return
        mint=int(input("Enter minute: "))
        if (mint>59) or (mint<0):
            speak("Invalid input entered sir. Terminating query.")
            print("Invalid minute")
            return
        speak("Enter 0 for am and 1 for pm")
        ampm=int(input("Enter 0 for am and 1 for pm: "))
        if ampm==0:
            ampm='am'
        elif ampm==1:
            ampm='pm'
        else:
            speak("Only valid input is 0 or 1. Query terminated.")
            print("Query dismissed...")
            return
    speak(f"Sir what message do want to leave for {alias_name}")
    msg=commandeng()
    if msg=="None":
        return
    speak("Once confirming message sir.")
    print("Message: ",msg)
    speak("Enter 0 for no and 1 for yes.")
    ch=int(input("Enter 1 for yes and 0 for no: "))
    if ch==1:
        ("Sorry sir something went wrong.")
    elif ch==0:
        speak("Okay sir then please enter message.")
        msg=input("Enter message: ")
        speak("Should i proceed now sir?")
        ch=commandeng()
        if ch=="None":
            return
        ch=cosine_sent(ch,['yes','no'])
        if 'yes' in ch:
            speak("Okay sir proceeding.")
        else:
            speak("Well ! dismissing query.")
            return
    else:
        speak("Sir due to invalid input we have to terminate this query.")
    if "professional" in cmd:
        msg="Hello, this is Cosmos, representing Ryan's artificial Wing. I am reaching out on behalf of Ryan.\n"+msg
    send_whatsapp_msg(alias_name,msg,hr,mint,ampm)

def ch31_func() -> None:
    '''whatsapp image'''
    speak("Sending a whatsapp image.")
    print('Raw whatsapp image messenger')
    alias_name=func_for_set5_1()
    if alias_name is None:
        return
    image_path=input("Enter path: ")
    speak("Add a caption to the image")
    image_caption=input("Caption: ")
    try:
        send_whatsapp_image(alias_name,image_path,image_caption)
    except Exception as e:
        speak("Error sending image. Check the path of image once.")
        print("Error: ",e)

def ch32_func(cmd: str) -> None:
    '''bulk message on whatsapp'''
    speak("Triggering bulk WhatsApp Message sequel.")
    print('Raw WhatsApp messenger')
    msg_list = []
    while True:
        all_alias = get_all_aliases()
        if all_alias is None:
            continue
        speak("Speak out the name whom you want to send a WhatsApp message.")
        alias_name = commandeng()
        if alias_name == "None":
            continue
        alias_name = match_word_func(alias_name, all_alias)
        if not alias_name:
            print("Sorry sir, something went wrong.")
            speak("Enter alias name.")
            alias_name = input("Enter alias name: ")
            alias_name = match_word_func(alias_name, all_alias)
            if not alias_name:
                print("No such alias name found.")
                continue
        msg_list.append(alias_name)
        speak("Do you want to add another recipient? Yes or no.")
        another_recipient = commandeng().lower()
        if another_recipient != 'yes':
            break
    speak("At what time do you want to send the message.")
    hr = int(input("Enter hour (12-hour format): "))
    if not (1 <= hr <= 12):
        speak("Invalid input entered, sir. Terminating query.")
        print("Invalid hour")
        return
    mint = int(input("Enter minute: "))
    if not (0 <= mint <= 59):
        speak("Invalid input entered, sir. Terminating query.")
        print("Invalid minute")
        return
    speak("Enter 0 for am and 1 for pm")
    ampm = int(input("Enter 0 for am and 1 for pm: "))
    if ampm == 0:
        ampm = 'am'
    elif ampm == 1:
        ampm = 'pm'
    else:
        speak("Only valid input is 0 or 1. Query terminated.")
        print("Query dismissed...")
        return
    speak("Sir, what message do you want to leave for the recipients?")
    msg = commandeng()
    if msg == "None":
        return
    speak("Once confirming the message, sir.")
    print("Message: ", msg)
    speak("Enter 0 for no and 1 for yes.")
    ch = commandeng()
    if ch == "None":
        return
    ch = cosine_sent(ch, ['yes', 'no'])
    if ch == 'yes':
        speak("Okay, sir. Proceeding.")
    else:
        msg = input("Enter the message: ")
        speak("Should I proceed now, sir?")
        ch = commandeng()
        if ch == "None":
            return
        ch = cosine_sent(ch, ['yes', 'no'])
        if ch == 'yes':
            speak("Okay, sir. Proceeding.")
        else:
            speak("Well! Dismissing query.")
            return
    if "professional" in cmd:
        msg = "Hello, this is Cosmos, representing Ryan's artificial intelligence. I am reaching out on behalf of Ryan.\n" + msg
    whatsapp_thread = threading.Thread(target=send_whatsapp_msg_toall, args=(msg_list, msg, hr, mint, ampm))
    whatsapp_thread.start()

def ch33_func() -> None:
    '''whatsapp message history'''
    speak("Showing whatsapp message history.")
    print('Message history: ')
    show_history_msg()

def ch34_func() -> None:
    '''ascii art'''
    speak("I may not be an expert in creating ASCII art, but let's give it a try!")
    print("ASCII art")
    path=input("Enter image path: ")
    image_to_ascii_art(path)

def ch35_func() -> None:
    '''screenshot'''
    speak("Taking a screenshot sir.")
    take_screenshot_pc()
    print("Screenshot saved at : (C:->Users->Admin->OneDrive->Pictures->Screenshot_by_Cosmos)")