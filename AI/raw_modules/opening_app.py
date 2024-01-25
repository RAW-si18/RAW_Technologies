# Updated 23/1/24

from AppOpener import open as oa
from raw_modules.speak_func import speak

def openapp(name: str) -> None:
    print(f'Opening {name}')
    success = oa(name, match_closest=True) 
    if success:
        speak('Application successfully opened')
        print('Application successfully opened')
    else:
        speak("Would you be interested in obtaining a comprehensive list of applications installed on your device?")
        print("Would you be interested in obtaining a comprehensive list of applications installed on your device?")
        choice = input("Y for yes & N for no: ")
        if choice.lower() == "y":
            oa("LS")
        elif choice.lower() == "n":
            exit()
        else:
            speak("Invalid input: Expecting a response of 'Y' for yes or 'N' for no. Defaulting to 'no' due to the invalid input.")
            print("Invalid input: Expecting a response of 'Y' for yes or 'N' for no. Defaulting to 'no' due to the invalid input.")
