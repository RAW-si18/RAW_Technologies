# Updated 23/1/24

from raw_modules.speak_func import *
from raw_modules.spttxt import *
from raw_modules.resume_cosmos import *
from raw_modules.calen_clock import *
from raw_modules.wikipedia_search import *
from raw_modules.city_name import *
from raw_modules.country_name import *
from raw_modules.climate_update import *

def ch_1_func() -> None:
    '''shutdown'''
    print("Procedure for initiating shutdown sequence!!")
    speak("Proceeding with shutdown. Confirming your request to turn off myself. Please respond with 'yes' to proceed or 'no' to keep me in sleep mode.")
    print("Please respond with 'yes' to proceed or 'no' to keep me in sleep mode.")
    shutdown_final=commandeng()
    if 'no' in shutdown_final:
        speak("Thank you sir,I will stay in sleep mode until further instructions. Feel free to awaken me when needed")
    elif 'yes' in shutdown_final:
        speak("Understood, sir. Initiating shutdown sequence for Cosmos AI. Disconnecting from all raw servers. Until next time, take care and feel free to turn me on whenever needed. Signing off.")
        print("COSMOS SHUTDOWN")
        exit()
    else:
        speak("Defaulting to shutdown process dismissed due to an error. Entering sleep mode. Feel free to call cosmos when needed.")

def ch1_func() -> None:
    '''cosmos introduction'''
    print("Cosmos Introduction generated")
    intro_cosmos()

def ch2_func() -> None:
    '''calendar'''
    print("Calendar flashed")
    cal_date,cal_month,cal_year,cal_day=calendar()
    speak(f"Today is {cal_date}, the {cal_day} of {cal_month}, in the year {cal_year}. Just another cosmic spin around the sun!")
    print(f"Today: {cal_date}-{cal_month}-{cal_year} (DD-MM-YYYY), {cal_day}")

def ch3_func() -> None:
    '''clock'''
    print("Clock popped up")
    clo_hr,clo_min,clo_sec,clo_st=clock()
    speak(f"Current time is {clo_hr} hour {clo_min} minutes {clo_st} and {clo_sec} seconds")
    print(f"{clo_hr}:{clo_min} {clo_st} and {clo_sec} seconds")

def ch4_func() -> None:
    '''city information'''
    print("City identification initiated by RAW")
    speak("Interested in exploring a specific city?")
    speak("Speak out the name of the city you're interested in")
    print('Name of city?')
    ct_name=commandeng()
    if ct_name=="None":
        return
    ct_property=city_name_function(ct_name)
    if ct_property==None:
        return
    speak(f"Oh want to know about {ct_property[0]}")
    print(f"CITY: {ct_property[0]}")
    print(f'Latitude: {ct_property[1]}')
    print(f'Longitude: {ct_property[2]}')
    print(f'Mother/Father country: {ct_property[3]},{ct_property[4]}')
    print(f'Population (*May 2023): {ct_property[5]}')
    print(f"Other things about {ct_property[0]}")
    wikipedia(ct_property[0])

def ch5_func() -> None:
    '''country information'''
    print("Country identification initiated by RAW")
    speak("Keen on discovering a captivating country?")
    speak("Speak out the name of the country you're interested in")
    print("Name of country?")
    cty_name=commandeng()
    if cty_name=="None":
        return
    cty_property=country_name_function(cty_name)
    if cty_property==None:
        return
    speak(f"Oh want to know about {cty_property[0]}")
    print(f"COUNTRY: {cty_property[0]}, {cty_property[2]}")
    print(f"Country code: {cty_property[1]}")
    print(f"Other things about {cty_property[0]}")
    wikipedia(cty_property[0])

def ch6_func() -> None:
    '''climate'''
    print("Climate Control RAW")
    speak("Hello! Interested in a climate update, sir? May I inquire about the specific city for which you'd like the current weather information?")
    print("City name?")
    city_climate=input("Enter city name: ")
    get_weather(city_climate)