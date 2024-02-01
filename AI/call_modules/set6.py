# Updated 26/1/24

from raw_modules.spttxt import commandeng
from raw_modules.speak_func import speak
from raw_modules.raw_messenger import sending_mail, playvideo_yt
from raw_modules.pc_shutdown import shutdown_pc,cancel_shutdown_pc
from raw_modules.steganography import image_hiding, image_unhide
import getpass, threading, csv
import pandas as pd
from raw_modules.raw_jokes import get_joke

def ch36_func() -> None:
    '''automate email'''
    speak("Preparing sequel for automating email.")
    speak("For sending mail should i use your personal account, raw account or fake account.")
    email_usage=commandeng()
    if email_usage=="None":
        return
    password=getpass.getpass("Enter laptop password: ")
    check=True
    while check==True:
        if password=='1234567':
            speak("Password verified successfully.")
            print("Password verified successfully.")
            break
        else:
            speak("Incorrect password.")
            print("Incorrect password.")
            check=False
    if check==False:
        speak("3 fail trials. Terminating query.")
        print("3 Failed Trials.")
        return
    subject=input("Subject/Title: ")
    message=input("Message: ")
    rec_email=input("Enter receiver's email: ")
    sending_mail(email_usage,subject,message,rec_email)

def ch37_func() -> None:
    '''youtube video'''
    speak("Here we go to search for a youtube video on a topic.")
    print("Youtube video")
    speak("What topic are you interested in exploring?")
    topic=commandeng()
    if topic=='None':
        return
    playvideo_yt(topic)

def ch38_func() -> None:
    '''shutdown sequel'''
    speak("Sequel for RAW-PC shutdown.")
    password=getpass.getpass("Enter laptop password: ")
    check=True
    while check==True:
        if password=='1234567':
            speak("Password verified successfully.")
            print("Password verified successfully.")
            break
        else:
            speak("Incorrect password.")
            print("Incorrect password.")
            check=False
    if check==False:
        speak("3 fail trials. Terminating query.")
        print("3 Failed Trials.")
        return
    shutdown_thread = threading.Thread(target=shutdown_pc, args=(30,))
    shutdown_thread.start()

def ch39_func() -> None:
    '''stop shutdown'''
    speak("Stopping PC shutown process.")
    cancel_shutdown_pc()

def ch_bug_func_1() -> None:
    '''bug sudden outbreak'''
    speak("Sir, a programming error is affecting the expected output. Urgent: Sudden outbreak forces immediate shutdown. ")
    speak("Ceasing Cosmos AI operations due to technical issues and the need for interpretation adjustments. Signing off...")
    print('Sudden outbreak shutdown initiated... ALERT!!')
    exit()

def ch_bug_func_2(e: str) -> None:
    '''minor bug error occured'''
    print("Error: ", e)
    speak("Sir, there seems to be an error in my programming, preventing the expected output. We are actively working to resolve this bug and anticipate a prompt solution.")
    error_df = pd.read_csv(r'H:\AI\resource_files\error_cosmos.csv')
    index = len(error_df) + 1
    speak("Sending a high alert feedback to RAW headquarters.")
    try:
        with open(r'H:\AI\resource_files\error_cosmos.csv', mode='a+', newline='') as error_file:
            writer = csv.writer(error_file)
            writer.writerows([[index,e]])
            speak("Successfully sent feedback for cosmos.")
            print("Feedback sent")
    except Exception as e:
        speak("Error in sending feedback due to some circumstances mentioned.")
        print(f"Error in sending feedback: {e}")
    speak("Reschedule to sleep mode")
    return

def ch40_func() -> None:
    speak("Hiding text in an image")
    print("Encryting text into image")
    speak("enter image path")
    st1=input("Image path: ")
    speak("enter text path")
    st2=input("Text path: ")
    speak("Please input the name of the file you wish to use for the encrypted image.")
    nam=input("Name: ")
    image_hiding(st1,st2,nam)
    print("Text hidden successfully.")

def ch41_func() -> None:
    speak("Raw decryption activated")
    speak("enter image path")
    st1=input("Image path: ")
    txt=image_unhide(st1)
    print("Decrypted text: \n\n")
    print(txt)

def ch42_func() -> None:
    get_joke()