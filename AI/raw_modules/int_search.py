# Updated 23/1/24

import subprocess
import webbrowser
from raw_modules.speak_func import speak

def internet_search(browser: str,query: str,mode: str) -> None:
    if mode == 'incognito':
        if browser == 'google':
            speak('Launch Google in incognito mode')
            print('Launch Google in incognito mode')
            subprocess.Popen(["C:/Program Files/Google/Chrome/Application/chrome.exe", "--incognito", f"https://www.google.com/search?q={query}" ])
        elif browser == 'brave':
            speak("Give a Brave mission—go incognito!'")
            print("Give a Brave mission—go incognito!'")
            webbrowser.open(f"https://search.brave.com/search?q={query}")
        elif browser == 'bing':
            speak("Explore Bing undercover - incognito mode activated!")
            print("Explore Bing undercover - incognito mode activated!")
            subprocess.Popen(["C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe", "--inprivate", f'https://www.bing.com/search?q={query}'])
        else:
            speak("Sorry, incognito mode for this search engine is not available at the moment.")
            print("Incognito for this search engine is not available")
            speak("Consider returning to the default Google mode for the incognito search experience?")
            print("Default to Google")
            choice=input("Y for yes & N for no")
            if choice.lower() == "y":
                internet_search('google',query,'incognito')
            elif choice.lower() == "n":
                exit()
            else:
                speak("Invalid input: Expecting a response of 'Y' for yes or 'N' for no. Defaulting to 'no' due to the invalid input.")
    else:
        if browser == 'bing':
            speak('Initiate on Bing')
            print('Initiate on Bing')
            webbrowser.open(f'https://www.bing.com/search?q={query}')
        elif browser == 'google':
            speak('Initiate the action on Google')
            print('Initiate the action on Google')
            webbrowser.open(f"https://www.google.com/search?q={query}")
        elif browser == 'brave':
            speak("Opening private Brave")
            print("Opening private Brave")
            webbrowser.open(f"https://search.brave.com/search?q={query}")
        else:
            speak('Regrettably, access to this search engine is currently unavailable.')
            print('Regrettably, access to this search engine is currently unavailable.')
            speak("Thinking about reverting to the classic Google mode for a more standard search journey?")
            print("Default to Google")
            choice=input("Y for yes & N for no")
            if choice.lower() == "y":
                internet_search('google',query,'standard')
            elif choice.lower() == "n":
                exit()
            else:
                speak("Invalid input: Expecting a response of 'Y' for yes or 'N' for no. Defaulting to 'no' due to the invalid input.")