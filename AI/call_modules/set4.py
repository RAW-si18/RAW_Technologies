# Updated 26/1/24

from raw_modules.speak_func import speak
from raw_modules.spttxt import commandeng
from raw_modules.extraction import extract_email, extract_humdata, extract_phone
from raw_modules.extra_funcs import webopen
from raw_modules.games import guess_number_game
from raw_modules.similar_sent import cosine_sent
from raw_modules.contacts import get_all_aliases, search_by_alias, update_contact_fav, update_contact_emergency
from raw_modules.similar_word import match_word_func

def ch22_func() -> None:
    '''email extraction'''
    speak("Initiating all email extraction from a file.")
    print("Email extraction from file")
    speak(r"Enter the file path sir, it should be in the format shown below.")
    link=input(r"Enter file path (Eg: R:\demo_cosmos\demo.txt): ")
    extract_email(link)

def ch23_func() -> None:
    '''phone number extraction'''
    speak("Initiating all Phone number extraction from a file.")
    print("Phone number extraction from file")
    speak(r"Enter the file path sir, it should be in the format shown below.")
    link=input(r"Enter file path (Eg: R:\demo_cosmos\demo.txt): ")
    extract_phone(link)

def ch24_func() -> None:
    '''human data extraction'''
    speak("Initiating all Human data extraction from a file.")
    print("Human data extraction from file")
    speak(r"Enter the file path sir, it should be in the format shown below.")
    link=input(r"Enter file path (Eg: R:\demo_cosmos\demo.txt): ")
    extract_humdata(link)

def ch25_func() -> None:
    '''open url of website'''
    speak("Want to open website using U.R.L..")
    print("Website URL opening...")
    speak("Enter U.R.L..")
    url_link=input("Enter URL: ")
    webopen(url_link)

def ch26_func() -> None:
    '''guessing game'''
    guess_number_game()

def ch27_func() -> None:
    '''fav contact update'''
    speak("Procedure to update favorite contact list.")
    print("Update Fav. contacts")
    all_alias=get_all_aliases()
    if all_alias==None:
        return
    alias_name=commandeng()
    alias_name=match_word_func(alias_name,all_alias)
    if not alias_name:
        print("Sorry sir something went wrong.")
        speak("Enter alias name.")
        alias_name=input("Enter alias name: ")
        alias_name=match_word_func(alias_name,all_alias)
        if not alias_name:
            print("No such alias name found.")
            return
    speak("To designate this contact as a favorite, respond with 'yes'; otherwise, reply with 'no.'")
    print("Yes for favorite contacts and No for non-favorite contacts")
    fav_ch=commandeng()
    fav_ch=cosine_sent(fav_ch,['yes','no'])
    if fav_ch==None:
        return
    elif fav_ch=='yes':
        fav_ch=1
    else:
        fav_ch=0
    update_contact_fav(alias_name,fav_ch)

def ch28_func() -> None:
    '''update emergency contacts'''
    speak("Procedure to update Emergency contact list.")
    print("Update emergency contacts")
    all_alias=get_all_aliases()
    if all_alias==None:
        return
    alias_name=commandeng()
    alias_name=match_word_func(alias_name,all_alias)
    if not alias_name:
        print("Sorry sir something went wrong.")
        speak("Enter alias name.")
        alias_name=input("Enter alias name: ")
        alias_name=match_word_func(alias_name,all_alias)
        if not alias_name:
            print("No such alias name found.")
            return
    speak("To designate this contact as a Emergency, respond with 'yes'; otherwise, reply with 'no.'")
    print("Yes for Emergency contacts and No for non-Emergency contacts")
    em_ch=commandeng()
    em_ch=cosine_sent(em_ch,['yes','no'])
    if em_ch==None:
        return
    elif em_ch=='yes':
        em_ch=1
    else:
        em_ch=0
    update_contact_emergency(alias_name,em_ch)

def ch29_func() -> None:
    '''search for alias name'''
    speak("Search for contact using alias name activated.")
    print("Search mode")
    all_alias=get_all_aliases()
    if all_alias==None:
        return
    alias_name=commandeng()
    alias_name=match_word_func(alias_name,all_alias)
    if not alias_name:
        print("Sorry sir something went wrong.")
        speak("Enter alias name.")
        alias_name=input("Enter alias name: ")
        alias_name=match_word_func(alias_name,all_alias)
        if not alias_name:
            print("No such alias name found.")
            return
    search_by_alias(alias_name)