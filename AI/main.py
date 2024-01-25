# Updated 23/1/24

print('RAW establishing server with cosmos 4.O!!\nLoading...')

#IMPORT ALL FUNCTIONS
from raw_modules.similar_sent import *
from raw_modules.similar_word import *
from raw_modules.raw_messenger import *
from raw_modules.pc_shutdown import *
from raw_modules.spttxt import *
from raw_modules.speak_func import *
import getpass
import threading

from raw_modules.switch_on import *
from raw_modules.sleeping import *
from call_modules.set1 import *
from call_modules.set2 import *
from call_modules.set3 import *
from call_modules.set4 import *
from call_modules.set5 import *
import csv

if __name__=="__main__":
    switch_on_msg()
# MAIN FUNCTION
    while True:
        try:
            while True:
                speak("Sleep mode activated sir!")
                print("Sleep mode Activated !!")
                choice,cmd=sleeping()
                if choice==(-1): # SHUTDOWN COSMOS
                    ch_1_func()
                elif choice==0: # None
                    continue
                elif choice==1: # Introduction of Cosmos
                    ch1_func()
                elif choice==2: # Calendar
                    ch2_func()
                elif choice==3: # Clock
                    ch3_func()
                elif choice==4: # City
                    ch4_func()
                elif choice==5: # Country
                    ch5_func()
                elif choice==6: # Climate
                    ch6_func()
                elif choice==7: # Get all contacts
                    ch7_func()
                elif choice==8: # Search name from contacts
                    ch8_func()
                elif choice==9: # Save a number in contacts
                    ch9_func()
                elif choice==10: # Delete a number from contact list
                    ch10_func()
                elif choice==11: # Update contact's phone number
                    ch11_func()
                elif choice==12: # Update contact's alias name
                    ch12_func()
                elif choice==13: # Search for RCI number in contacts
                    ch13_func()
                elif choice==14: # Complete contacts
                    ch14_func()
                elif choice==15: # Internet search on search engine
                    ch15_func(cmd)
                elif choice==16: # open an app on desktop
                    ch16_func()
                elif choice==17: # Greet me
                    ch17_func()
                elif choice==18: # Set an alarm
                    ch18_func(cmd)
                elif choice==19: # Predict logic wise-similar sentence
                    ch19_func()
                elif choice==20: # Predict spelling wise-similar words
                    ch20_func()
                elif choice==21: # Wikipedia search
                    ch21_func(cmd)
                elif choice==22: # Email extraction from file
                    ch22_func()
                elif choice==23: # Ph. No. extraction from file
                    ch23_func()
                elif choice==24: # Humdata extraction from file
                    ch24_func()
                elif choice==25: # URL website
                    ch25_func()
                elif choice==26: # Guess a number game
                    ch26_func()
                elif choice==27: # Update favorite list
                    ch27_func()
                elif choice==28: # Update Emergency list
                    ch28_func()
                elif choice==29: # Search for contacts using alias name
                    ch29_func()
                elif choice==30: # Send a whatsapp message
                    ch30_func(cmd)
                elif choice==31: # Send a whatsapp image
                    ch31_func(cmd)
                elif choice==32: # Send bulk whatsapp message
                    speak("Triggering bulk WhatsApp Message sequel.")
                    print('Raw whatsapp messenger')
                    msg_list=[]
                    while True:
                        all_alias=get_all_aliases()
                        if all_alias==None:
                            continue
                        speak("Speak out the name whom you want to send whatsapp message.")
                        alias_name=commandeng()
                        if alias_name=="None":
                            continue
                        alias_name=match_word_func(alias_name,all_alias)
                        if not alias_name:
                            print("Sorry sir something went wrong.")
                            speak("Enter alias name.")
                            alias_name=input("Enter alias name: ")
                            alias_name=match_word_func(alias_name,all_alias)
                            if not alias_name:
                                print("No such alias name found.")
                                continue
                        msg_list.append(alias_name)
                    speak("At what time do you want to send message.")
                    hr=int(input("Enter hour (12 hour format): "))
                    if (hr>12) or (hr<1):
                        speak("Invalid input entered sir. Terminating query.")
                        print("Invalid hour")
                        continue
                    mint=int(input("Enter minute: "))
                    if (mint>59) or (mint<0):
                        speak("Invalid input entered sir. Terminating query.")
                        print("Invalid minute")
                        continue
                    speak("Enter 0 for am and 1 for pm")
                    ampm=int(input("Enter 0 for am and 1 for pm: "))
                    if ampm==0:
                        ampm='am'
                    elif ampm==1:
                        ampm='pm'
                    else:
                        speak("Only valid input is 0 or 1. Query terminated.")
                        print("Query dismissed...")
                        continue
                    speak(f"Sir what message do want to leave for {alias_name}")
                    msg=commandeng()
                    if msg=="None":
                        continue
                    speak("Once confirming message sir.")
                    print("Message: ",msg)
                    ch=commandeng()
                    if ch=="None":
                        continue
                    ch=cosine_sent(ch,['yes','no'])
                    if ch=='yes':
                        speak("Okay sir proceeding.")
                    else:
                        msg=input("Enter message: ")
                        speak("Should i proceed now sir?")
                        ch=commandeng()
                        if ch=="None":
                            continue
                        ch=cosine_sent(ch,['yes','no'])
                        if ch=='yes':
                            speak("Okay sir proceeding.")
                        else:
                            speak("Well ! dismissing query.")
                            continue
                    if "professional" in cmd:
                        msg="Hello, this is Cosmos, representing Ryan's artificial intelligence. I am reaching out on behalf of Ryan.\n"+msg
                    whatsapp_thread = threading.Thread(target=send_whatsapp_msg_toall, args=(msg_list,msg,hr,mint,ampm))
                    whatsapp_thread.start()
                elif choice==33: # Whatsapp message history
                    speak("Showing whatsapp message history.")
                    print('Message history: ')
                    show_history_msg()
                elif choice==34: # image ascii
                    speak("I may not be an expert in creating ASCII art, but let's give it a try!")
                    print("ASCII art")
                    image_path=input("Enter image path: ")
                    image_ascii(image_path)
                elif choice==35: # Take screenshot
                    speak("Taking a screenshot sir.")
                    take_screenshot_pc()
                    print("Screenshot saved at : (C:->Users->Admin->OneDrive->Pictures->Screenshot_by_Cosmos)")
                elif choice==36: # Sending Email
                    speak("Preparing sequel for automating email.")
                    speak("For sending mail should i use your personal account, raw account or fake account.")
                    email_usage=commandeng()
                    if email_usage=="None":
                        continue
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
                        continue
                    subject=input("Subject/Title: ")
                    message=input("Message: ")
                    rec_email=input("Enter receiver's email: ")
                    sending_mail(email_usage,subject,message,rec_email)
                elif choice==37: # Play youtube video
                    speak("Here we go to search for a youtube video on a topic.")
                    print("Youtube video")
                    speak("What topic are you interested in exploring?")
                    topic=commandeng()
                    if topic=='None':
                        continue
                    playvideo_yt(topic)
                elif choice==38: # Shutdown pc
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
                        continue
                    shutdown_thread = threading.Thread(target=shutdown_pc, args=(30,))
                    shutdown_thread.start()
                elif choice==39: # Shutdown pc cancel
                    speak("Stopping PC shutown process.")
                    cancel_shutdown_pc()
                else: # Extreme Bug case
                    speak("Sir, a programming error is affecting the expected output. Urgent: Sudden outbreak forces immediate shutdown. ")
                    speak("Ceasing Cosmos AI operations due to technical issues and the need for interpretation adjustments. Signing off...")
                    print('Sudden outbreak shutdown initiated... ALERT!!')
                    exit()
        except Exception as e:
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
            continue
