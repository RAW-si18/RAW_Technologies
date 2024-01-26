# Updated 26/1/24

from raw_modules.speak_func import speak
from raw_modules.spttxt import commandeng
from raw_modules.contacts import get_all_aliases, search_names, contact_save, delete_contact_by_alias
from raw_modules.contacts import update_contact_phone, update_alias, show_data_rci, show_whole_table
from raw_modules.remove_duplicate import remove_duplicate_words
from raw_modules.country_name import country_name_function
from raw_modules.similar_word import match_word_func

def ch7_func() -> None:
    '''display alias names'''
    print("Displaying all contacts alias name")
    speak("Displaying contact alias name from the raw database, sir.")
    alias_list=get_all_aliases()
    if alias_list==None:
        return
    for i in alias_list:
        print(i)

def ch8_func() -> None:
    '''search for contacts'''
    print("Searching name in contacts")
    speak("Searching for full name in contacts")
    f_name=input("Enter first name: ")
    l_name=input("Enter last name: ")
    search_names(f_name,l_name)

def ch9_func() -> None:
    '''save contact'''
    speak("The process of saving contacts in the raw database has been initiated.")
    print("Procedure to save contacts initiated.")
    speak("Enter phone number.")
    ph_no=int(input("Enter phone number: "))
    speak("Enter first name.")
    f_name=input("Enter first name: ") 
    speak("Enter last name.")
    l_name=input("Enter last name: ")  
    speak("In which country does the person, whose contact you are saving, reside?")
    c_name=commandeng()
    c_name=remove_duplicate_words(c_name)
    c_property=country_name_function(c_name)
    if c_property==None:
        return
    print(f"Country name: {c_property[0]}")
    c_code=c_property[1]   
    speak(f"What alias name do you want to assign to {f_name} {l_name}?")
    alias_name=commandeng()
    speak(f"Confirm saving this contact as '{alias_name}'-reply 'yes' to proceed or 'no' to cancel.")
    trial_ch=commandeng()
    trial_ch=match_word_func(trial_ch,['yes','no'])
    if not trial_ch:
        speak("Apologies, sir. Since I couldn't understand a clear 'yes' or 'no,' I'm defaulting to 'no.' Please type the alias name you want to assign to the contact.")
        alias_name=input("Enter alias name: ")
    elif trial_ch=='no':
        speak("Apologies for the confusion. Please provide the correct alias name.")
        alias_name=input("Enter alias name: ") 
    else:
        speak(f"Alias name is {alias_name}")
    speak("Should this contact be added to the favorites list?")
    trial_ch=commandeng()
    trial_ch=match_word_func(trial_ch,['yes','no'])
    if trial_ch=='yes':
        speak("Successfully added to favorite list in contacts.")
        fav_ch=1
    elif trial_ch=='no':
        speak("Okay sir not adding in favorite list of contacts.")
        fav_ch=0
    else:
        speak("Apologies for any confusion, sir. Defaulting to 'not in favorites' due to my lack of understanding.")
        fav_ch=0
    speak("Should this contact be added to the emergency list?")
    trial_ch=commandeng()
    trial_ch=match_word_func(trial_ch,['yes','no'])
    if trial_ch=='yes':
        speak("Successfully added to emergency list in contacts.")
        em_ch=1
    elif trial_ch=='no':
        speak("Okay sir not adding in emergency list of contacts.")
        em_ch=0
    else:
        speak("Apologies for any confusion, sir. Defaulting to 'not in emergency' due to my lack of understanding.")
        em_ch=0
    speak("Please review all details and confirm by typing 'yes' or 'no'.")
    print(f"Name: {f_name} {l_name} ({alias_name})\nPh.No.: +{c_code} {ph_no}")
    if (fav_ch==0 and em_ch==0):
        print("Not a favorite or emergency contact")
    elif (fav_ch==1 and em_ch==0):
        print("Favorite but not emergency contact")
    elif (fav_ch==0 and em_ch==1):
        print("Emergency but not favorite contact")
    else:
        print("Both favorite and emergency contact")
    trial_ch=commandeng()
    trial_ch=match_word_func(trial_ch,['yes','no'])
    if trial_ch=='yes':
        speak("Yes confirmed")
        trial_ch=1
    elif trial_ch=='no':
        speak("No confirmed... Terminating query.")
        trial_ch=0
        return
    else:
        speak("Apologies for any confusion, sir can you please type 1 for yes or 0 for no.")
        trial_ch=int(input("Enter 1 for yes and 0 for no: "))
        if trial_ch==0:
            speak("No has been confirmed terminating...")
            print("Confirmed NO")
            return
        elif trial_ch==1:
            speak("Yes confirmed. adding to database.")
        else:
            speak("Only 0 or 1 is valid... terminating query.")
            print("Only 0 or 1 is valid... terminating query.")
            return
    contact_save(f_name,l_name,c_code,ph_no,alias_name,fav_ch,em_ch)

def ch10_func() -> None:
    '''delete contact'''
    speak("Deleting contact procedure initiated.")
    print("Contact Delete procedure activated.")
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
    speak(f"Alias name to be deleted is {alias_name}")
    trial_ch=commandeng()
    trial_ch=match_word_func(trial_ch,['yes','no'])
    if trial_ch=='yes':
        speak("Yes confirmed")
    elif trial_ch=='no':
        speak("No confirmed... Terminating query.")
        return
    else:
        speak("Apologies for confusion, defaulting to no. Query dismissed.")
        print("Query dismissed!!")
        return
    delete_contact_by_alias(alias_name)

def ch11_func() -> None:
    '''update phone number'''
    speak("Update phone number using alias name") 
    print("Update phone number using alias name") 
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
    speak(f"Phone number to be updated is of {alias_name}")
    trial_ch=commandeng()
    trial_ch=match_word_func(trial_ch,['yes','no'])
    if trial_ch=='yes':
        speak("Yes confirmed")
    elif trial_ch=='no':
        speak("No confirmed... Terminating query.")
        return
    else:
        speak("Apologies for confusion, defaulting to no. Query dismissed.")
        print("Query dismissed!!")
        return
    new_ph=int(input("Enter new phone number: "))
    update_contact_phone(alias_name,new_ph)

def ch12_func() -> None:
    '''update alias name'''
    speak("Update Alias name.") 
    print("Update alias name activated") 
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
    speak(f"Alias name to be updated is of {alias_name}")
    trial_ch=commandeng()
    trial_ch=match_word_func(trial_ch,['yes','no'])
    if trial_ch=='yes':
        speak("Yes confirmed")
    elif trial_ch=='no':
        speak("No confirmed... Terminating query.")
        return
    else:
        speak("Apologies for confusion, defaulting to no. Query dismissed.")
        print("Query dismissed!!")
        return
    new_alias=input("Enter new alias name: ")
    update_alias(alias_name,new_alias)

def ch13_func() -> None:
    '''data of rci number'''
    speak("Data of R.C.I. number")
    print("Search for data using R.C.I.")
    rci=int(input("Enter rci number: "))
    show_data_rci(rci)

def ch14_func() -> None:
    '''complete contact list'''
    speak("Traverse through complete contact list.")
    print('Complete contact list displayed: ')
    show_whole_table()