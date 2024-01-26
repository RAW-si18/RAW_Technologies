# Updated 23/1/24

from raw_modules.similar_word import match_word_func
from raw_modules.speak_func import speak
import pandas as pd
from typing import Optional, Union, List

def country_name_function(country_name: str) -> Optional[List[Union[str, int]]]:
    '''country name from database'''
    df=pd.read_csv("H:\\AI\\resource_files\\country_codes.csv",encoding='latin1',header=0)
    country_name=match_word_func(country_name,df['country'])
    if not country_name:
        speak(f"No exact matches found.")
        print(f"No exact matches found.")
        return None
    if len(country_name)==1:
        country_name=country_name[0]
    else:
        speak("I apologize, sir, but I am having difficulty determining the correct country name.\nCould you please inform me which one of the following options is the closest match?\nIf none of the options matches, kindly specify 'none'.")
        j=1
        for i in country_name:
            print(f"country {j}: {i}")
            j+=1
        speak(f"Please enter {j} if none of the above options align with your preference.")
        print(f"Please enter {j} if none of the above options align with your preference.")
        country_name.append("none")
        check=int(input("Enter the option number for your desired country: "))
        if check>j:
            speak(f"Oops! Looks like you took a detour to the land of invalid inputs. Only choices 1 to {j} are invited to the party!")
        country_name=country_name[check-1]
        if country_name=="none":
            speak("Apologies, sir. I couldn't determine the country name. We're terminating this query.\nPlease double-check the country name.")
            return None
    c_initial=df.loc[df['country'] == country_name, 'initial'].iloc[0]
    c_code=df.loc[df['country'] == country_name, 'code'].iloc[0]
    return [country_name,c_code,c_initial]