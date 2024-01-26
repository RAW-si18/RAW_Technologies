# Updated 26/1/24

print('RAW establishing server with cosmos 4.O!!\nLoading...')

#IMPORT ALL FUNCTIONS
from raw_modules.switch_on import switch_on_msg
from raw_modules.sleeping import sleeping
from call_modules.set1 import *
from call_modules.set2 import *
from call_modules.set3 import *
from call_modules.set4 import *
from call_modules.set5 import *
from call_modules.set6 import *

if __name__=="__main__":
    switch_on_msg()
# MAIN FUNCTION
    while True:
        try:
            while True:
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
                    ch31_func()
                elif choice==32: # Send bulk whatsapp message
                    ch32_func(cmd)
                elif choice==33: # Whatsapp message history
                    ch33_func()
                elif choice==34: # image ascii
                    ch34_func()
                elif choice==35: # Take screenshot
                    ch35_func()
                elif choice==36: # Sending Email
                    ch36_func()
                elif choice==37: # Play youtube video
                    ch37_func()
                elif choice==38: # Shutdown pc
                    ch38_func()
                elif choice==39: # Shutdown pc cancel
                    ch39_func()
                else: # Extreme Bug case
                    ch_bug_func_1()
        except Exception as e:
            ch_bug_func_2()