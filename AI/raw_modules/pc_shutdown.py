# Updated 23/1/24

import os
import platform
import winerror
from raw_modules.speak_func import speak

osname = platform.system()

def shutdown_pc(time=30) -> None:
    '''shutdown pc'''
    if "windows" in osname.lower():
        error_code = os.system(f"shutdown -s -t {time}")
        if error_code in [winerror.ERROR_SHUTDOWN_IN_PROGRESS, 1115]:
            speak("Sir shutdown process for RAW laptop has already been Scheduled!")
            print("Already, shutdown PC initiated.")
        else:
            speak(f"Sir, RAW System will Shutdown in {time} Seconds!")
            print(f"RAW System will Shutdown in {time} Seconds!")
    elif "linux" in osname.lower():
        os.system(f"shutdown -h {time}")
        speak(f"RAW System will Shutdown in {time} Minutes!")
        print(f"RAW System will Shutdown in {time} Minutes!")
    elif "darwin" in osname.lower():
        os.system(f"shutdown -h -t {time}")
        speak(f"RAW System will Shutdown in {time} Minutes!")
        print(f"RAW System will Shutdown in {time} Minutes!")
    else:
        speak(f"Sorry sir, available on Windows, Mac O.S. and Linux only, can't Execute on {osname}")
        print(f"Available on Windows, MacOS and Linux only, can't Execute on {osname}")

def cancel_shutdown_pc() -> None:
    '''cancel shutdown pc process'''
    if "windows" in osname.lower():
        error_code = os.system("shutdown /a")
        if error_code == winerror.ERROR_NO_SHUTDOWN_IN_PROGRESS:
            speak("Sir, Shutdown Cancellation process has been Aborted!")
            print("Shutdown Cancellation process has been Aborted! [NO Shutdown Scheduled]")
        else:
            speak("sir, Shutdown has been Cancelled sir!")
            print("Shutdown has been Cancelled!")
    elif "linux" in osname.lower():
        os.system("shutdown -c")
        speak("Sir, Shutdown has been Cancelled sir!")
        print("Shutdown has been Cancelled!")
    elif "darwin" in osname.lower():
        os.system("killall shutdown")
        speak("Sir, Shutdown has been Cancelled sir!")
        print("Shutdown has been Cancelled!")
    else:
        speak(f"Available on Windows, Mac and Linux only, can't Execute on {osname}")
        print(f"Available on Windows, Mac and Linux only, can't Execute on {osname}")
