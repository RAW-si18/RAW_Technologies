# UPDATED 23/1/24 (UPDATE NOT REQUIRED)

import pyautogui ,re ,smtplib, requests
import webbrowser
from email.message import EmailMessage
from email.mime.text import MIMEText
import threading
from raw_modules.calen_clock import *
from raw_modules.speak_func import speak
from raw_modules.contacts import search_by_alias
from raw_modules.similar_sent import cosine_sent
from raw_modules.whats import *
from raw_modules.ascii_art import image_to_ascii_art

def send_whatsapp_msg(alias_name: str,msg: str,hr: int,mint: int,ampm: str) -> None:
    '''send whatsapp message'''
    if ampm.lower() == "pm" and hr != 12:
        hr += 12
    elif ampm.lower() == "am" and hr == 12:
        hr = 0
    detail=search_by_alias(alias_name)
    if detail==None:
        return
    ph_number=f"+{detail[3]}{detail[4]}"
    speak(f"Whatsapp message scheduled for {hr}:{mint} sir.")
    whatsapp_thread = threading.Thread(target=sendwhatmsg, args=(ph_number, msg, hr, mint,10,True,2))
    whatsapp_thread.start()

def send_whatsapp_image(alias_name: str,image_path: str,image_caption: str) -> None:
    '''send image on whatsapp'''
    detail=search_by_alias(alias_name)
    if detail==None:
        return
    ph_number=f"+{detail[3]}{detail[4]}"
    speak("Sending image initiated.")
    sendwhats_image(ph_number,image_path,image_caption,10,True,2)

def send_whatsapp_msg_toall(alias_list: list,msg: str,hr: int,mint: int,ampm: str) -> None:
    if ampm.lower() == "pm" and hr != 12:
        hr += 12
    elif ampm.lower() == "am" and hr == 12:
        hr = 0
    ph_list=[]
    for i in range(len(alias_list)):
        detail=search_by_alias(alias_list[i])
        if detail==None:
            return
        ph_number=f"+{detail[3]}{detail[4]}"
        ph_list.append(ph_number)
    speak("Whatsapp message scheduled sir.")
    whatsapp_mul=threading.Thread(target=whatsapp_multiple_open,args=(ph_list, msg, hr, mint))
    whatsapp_mul.start()

def whatsapp_multiple_open(phone_list: list, msg: str, hr: int, mint: int) -> None:
    sendwhatmsg(phone_list[0], msg, hr, mint, 10, True, 2)
    for i in range(len(phone_list)-1):
        time.sleep(2)
        sendwhatmsg_instantly(phone_list[i+1],msg,6,True,2)
        pyautogui.press("enter")

def show_history_msg():
    speak("Showing history of whatsapp using Cosmos AI.")
    show_history()

def image_ascii(path):
    speak("Creating an Artistic Image to ASCII art.")
    image_to_ascii_art(path)
    speak("Created a small art for you sir.")

def take_screenshot_pc():
    screenshot = pyautogui.screenshot()
    cal_temp=calendar()
    cal_temp=list(cal_temp)
    clock_temp=clock()
    clock_temp=list(clock_temp)
    ss=f"\\ss_{cal_temp[0]}{cal_temp[1]}{cal_temp[2]}_{clock_temp[0]}{clock_temp[1]}{clock_temp[2]}_{clock_temp[3]}"
    ss=f"C:\\Users\\Admin\\OneDrive\\Pictures\\Screenshot_by_Cosmos{ss}.png"
    screenshot.save(ss)
    speak("Done sir.")

def sending_mail(email_usage,subject,message,email_receiver):
    speak("Sending automated mail")
    email_usage=cosine_sent(email_usage,["personal account","coding/company RAW account","fake account"])
    if email_usage=="personal account":
        email_sender="ryanmadhuwala05@gmail.com"
        password="flkx uitr tsan igju"
    elif email_usage=="coding/company RAW account":
        email_sender="intelligencecosmos@gmail.com"
        password="totm oujl ooje iyrt"
    else:
        email_sender="tecrtg@gmail.com"
        password="qgwg gmik eowh osqb"
    domain = re.search("(?<=@)[^.]+(?=\\.)", email_sender)
    hostnames = {
        "gmail": "smtp.gmail.com",
        "yahoo": "smtp.mail.yahoo.com",
        "outlook": "smtp.live.com",
        "aol": "smtp.aol.com",
    }
    hostname = hostnames.get(domain.group())
    if hostname is None:
        speak("Sir, this email ID is not currently supported")
        print(f"{domain.group()} is not Supported Currently!")
    try:
        with smtplib.SMTP_SSL(hostname, 465) as smtp:
            smtp.login(email_sender, password)
            msg = EmailMessage()
            msg["Subject"] = subject
            msg["From"] = email_sender
            msg["To"] = email_receiver
            if isinstance(message, str):
                msg.set_content(message)
            elif isinstance(message, MIMEText):
                msg = message
            smtp.send_message(msg)
            speak("Email has been sent successfully.")
            print("Email Sent Successfully!")
            return True
    except Exception as e:
        speak("Sorry sir, Email sending procedure failed.")
        print(f"Failed to send email: {e}")
        return False

def playvideo_yt(topic):
    url = f"https://www.youtube.com/results?q={topic}"
    count = 0
    cont = requests.get(url, timeout=5)
    data = str(cont.content)
    lst = data.split('"')
    ch=1
    ch_list=[]
    speak("Sir, below are some related videos.")
    print("Related videos: ")
    for i in lst:
        count += 1
        if i == "WEB_PAGE_TYPE_WATCH":
            print("\n",ch,".",lst[count - 27])
            ch+=1
            if lst[count - 5] == "/results":
                speak("Sorry sir, no related videos found.")
                print("No Video Found for this Topic!")
                break
            ch_list.append(lst[count - 5])
            if ch>10:
                break
    print("")
    speak("Enter serial number of your choice video.")
    opt=int(input("Enter serial number: "))
    if 1<opt<=11:
        speak("Opening video.")
        webbrowser.open(f"https://www.youtube.com{ch_list[opt-1]}")
    else:
        speak("Sorry sir, invalid serial number entered. Opening first video.")
        print("Invalid serial number entered.")
        webbrowser.open(f"https://www.youtube.com{ch_list[0]}")