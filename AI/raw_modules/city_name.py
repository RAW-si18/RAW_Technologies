# Updated 23/1/24

from raw_modules.similar_word import match_word_func
from raw_modules.speak_func import speak
from typing import List
import pandas as pd

def city_name_function(city_name_input: str) -> List[str, int ,int, str, str, int]:
    '''city name from database'''
    df=pd.read_csv(r"H:\AI\resource_files\city_codes.csv",encoding='latin1',header=0)
    city_name=match_word_func(city_name_input,df['city'])
    if city_name==None:
        speak("No exact matches found.")
        print("No match")
        return None
    if len(city_name)==1:
        city_name=city_name[0]
    else:
        if city_name[0]==city_name_input.capitalize():
            city_name=city_name[0]
        elif city_name[1]==city_name_input.capitalize():
            city_name=city_name[1]
        elif city_name[2]==city_name_input.capitalize():
            city_name=city_name[2]
        else:
            speak("I apologize, sir, but I am having difficulty determining the correct city name.\nCould you please inform me which one of the following options is the closest match?\nIf none of the options matches, kindly specify 'none'.")
            j=1
            for i in city_name:
                print(f"city {j}: {i}")
                j+=1
            print(f"Please enter {j} if none of the above options align with your preference.")
            speak(f"Please enter {j} if none of the above options align with your preference.")
            city_name.append("none")
            check=int(input("Enter the option number for your desired city: "))
            if check>j:
                speak(f"Oops! Looks like you took a detour to the land of invalid inputs. Only choices 1 to {j} are invited to the party!")
                print("Query dismissed")
                return None
            city_name=city_name[check-1]
            if city_name=="none":
                speak("Apologies, sir. I couldn't determine the city name. We're terminating this query.\nPlease double-check the city name.")
                return None
    c_lat=df.loc[df['city'] == city_name, 'latitude'].iloc[0]
    c_lon=df.loc[df['city'] == city_name, 'longitude'].iloc[0]
    c_country=df.loc[df['city'] == city_name, 'country'].iloc[0]
    c_initial=df.loc[df['city'] == city_name, 'country_code'].iloc[0]
    c_population=df.loc[df['city'] == city_name, 'population'].iloc[0]
    city_properties=[city_name,c_lat,c_lon,c_country,c_initial,c_population]
    return city_properties