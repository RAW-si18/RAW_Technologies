# Updated 23/1/24

import pandas as pd
from raw_modules.similar_word import match_word_func
from raw_modules.spttxt import commandeng
import mysql.connector as myc
from raw_modules.speak_func import speak
import os
from typing import Optional, List, Union

def get_all_aliases() -> Optional[List[str]]:
    ''' get all alias name from database'''
    mydb = myc.connect(host='localhost', user='root', password='cosmos18', database='raw')
    cur = mydb.cursor()
    select_query = "SELECT alias FROM contacts"
    try:
        cur.execute(select_query)
        aliases = [row[0] for row in cur.fetchall()] 
        return aliases
    except myc.Error as e:
        print(f'Error fetching aliases: {e}')
        return None
    finally:
        mydb.close()

def search_by_alias(alias_name_input: str) -> Optional[List[Union[str,int]]]:
    '''search from database for alias name'''
    alias_list = get_all_aliases()
    if alias_list is None:
        speak("No matches found.")
        print("No matches found.")
        return None
    alias_name = match_word_func(alias_name_input, alias_list)
    if len(alias_name) == 1:
        alias_name = alias_name[0]
    else:
        if alias_name[0] == alias_name_input.lower():
            alias_name = alias_name[0]
        elif alias_name[1] == alias_name_input.lower():
            alias_name = alias_name[1]
        elif alias_name[2] == alias_name_input.lower():
            alias_name = alias_name[2]
        else:
            speak("I apologize, sir, but I am having difficulty determining the correct alias name.\nCould you please inform me which one of the following options is the closest match?\nIf none of the options matches, kindly specify 'none'.")
            j = 1
            for i in alias_name:
                print(f"Alias {j}: {i}")
                j += 1
            print(f"Please enter {j} if none of the above options align with your preference.")
            speak(f"Please enter {j} if none of the above options align with your preference.")
            alias_name.append("none")
            check = int(input("Enter the option number for your desired alias: "))
            if check == 1:
                alias_name = alias_name[check - 1]
            elif check == 2:
                alias_name = alias_name[check - 1]
            elif check == 3:
                alias_name = alias_name[check - 1]
            else:
                speak("Apologies, sir. Please review the entire contact list and return later.")
                return None
    mydb = myc.connect(host='localhost', user='root', password='cosmos18', database='raw')
    cur = mydb.cursor()
    select_query = "SELECT * FROM contacts WHERE alias = %s"
    try:
        cur.execute(select_query, (alias_name,))
        result = cur.fetchone()
    except Exception as e:
        print(f'Error searching by alias: {e}')
        return None
    finally:
        mydb.close()
    if result:
        print("Found matching contact:")
        print(f"RCI ID: {result[0]}")
        print(f"First Name: {result[1]}")
        print(f"Last Name: {result[2]}")
        print(f"Phone number: +{result[3]} {result[4]}")
        print(f"Alias name: {result[5]}")
        return [result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7]]
    else:
        print("Match not found... Review complete contacts list")
        return None

def search_names(first_name: str, last_name: str) -> None:
    '''search for first + last name'''
    mydb = myc.connect(host='localhost', user='root', password='cosmos18', database='raw')
    cur = mydb.cursor()
    select_query = "SELECT first_name, last_name FROM contacts"
    try:
        cur.execute(select_query)
        names = [(row[0], row[1]) for row in cur.fetchall()]
    except Exception as e:
        speak("Error searching names, review the error below")
        print(f'Error searching names: {e}')
        return
    found_match = False
    for i in range(len(names)):
        if first_name.lower() in names[i][0].lower() and last_name.lower() in names[i][1].lower():
            found_match = True
            cur.execute("SELECT contact_id FROM contacts WHERE first_name=%s AND last_name=%s", (names[i][0], names[i][1]))
            cont_id = [i[0] for i in cur.fetchall()]
            print("Found matching RAW Corporate ID")
            speak("Found matching RAW Corporate ID")
            for i in cont_id:
                print(f"RCI: {i}")
            break
    if not found_match:
        speak("Oh dear! It seems like your contact list is playing hide-and-seek.")
        speak("Sir, could you please take a moment to review the complete contacts list.")
        print("Match not found... Review complete contacts list")
    mydb.close()

def contact_save(f_name: str,l_name: str,country_code: int,ph_no: int,alias: str,fav_cont: int,emergency_cont: int) -> None:
    '''save contacts in database'''
    mydb=myc.connect(host='localhost',user='root',password='cosmos18',database='raw')
    cur=mydb.cursor()
    insval="INSERT INTO contacts (first_name ,last_name ,country_code ,phone_number ,alias , is_favorite, is_emergency_contact) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    vallist=(f_name,l_name,country_code,ph_no,alias,fav_cont,emergency_cont)
    try:
        cur.execute(insval,vallist)
        mydb.commit()
        print('Contact successfully inserted')
        speak('Contact successfully inserted')
    except Exception as e:
        speak('Contact storage failed please try again in few minutes\n')
        print("Contact storage failed please try again in few minutes\nError: ",e)
        mydb.rollback()
    finally:
        mydb.close()

def delete_contact_by_alias(alias: str) -> None:
    '''delete contacts using alias name'''
    all_aliases = get_all_aliases()
    if all_aliases==None:
        return
    matches = match_word_func(alias, all_aliases)
    if not matches:
        speak(f"No exact matches found for '{alias}'.")
        print(f"No exact matches found for '{alias}'.")
        return
    if len(matches) == 1:
        matched_alias = matches[0]
    else:
        speak("I apologize, but I am having difficulty determining the correct alias.")
        print("Could you please inform me which one of the following options is the closest match?")
        speak("Could you please inform me which one of the following options is the closest match?")
        for i in matches:
            print(f"Alias: {i}")
        matches.append("none")
        check = commandeng()
        matched_alias = match_word_func(check, matches)
        if matched_alias is None or matched_alias == "none":
            speak("Apologies, I couldn't determine the alias. Terminating this query.")
            speak("Please double-check the alias, and I'll provide a list for verification.")
            print("Please double-check the alias, and I'll provide a list for verification.")
            for i in all_aliases:
                print(f"Alias: {i}")
            return
        matched_alias = matched_alias[0]
    print(f"Alias: {matched_alias}")
    mydb = myc.connect(host='localhost', user='root', password='cosmos18', database='raw')
    cur = mydb.cursor()
    try:
        delete_query = "DELETE FROM contacts WHERE alias = %s"
        cur.execute(delete_query, (matched_alias,))
        mydb.commit()
        speak(f"Record successfully deleted for Alias: {matched_alias}")
        print(f"Record successfully deleted for Alias: {matched_alias}")
    except Exception as e:
        speak("Deletion failed.")
        print(f"Deletion failed: {e}")
        mydb.rollback()
    finally:
        mydb.close()

def update_contact_phone(alias: str, new_phone_number: int) -> None:
    '''update to new phone number'''
    list_alias=get_all_aliases()
    if list_alias==None:
        return
    alias=match_word_func(alias,list_alias)
    if not alias:
        print(f"No exact match found.")
        return
    if len(alias)==1:
        alias=alias[0]
    else:
        print("I apologize, sir, but I am having difficulty determining the correct Alias name.\nCould you please inform me which one of the following options is the closest match?\nIf none of the options matches, kindly specify 'none'.")
        for i in alias:
            print(f"Alias: {i}")
        alias.append("none")
        check=commandeng()
        alias=match_word_func(check,alias)
        if alias=="none":
            print("Apologies, sir. I couldn't determine the Alias name. We're terminating this query.\nPlease double-check the alias name, and I'll provide a list for verification.")
            for i in list_alias:
                print(i)
            return
        if len(alias)!=1:
            print("Apologies, sir. I couldn't determine the Alias name. We're terminating this query.\nPlease double-check the alias name, and I'll provide a list for verification.")
            for i in list_alias:
                print(i)
            return
        alias=alias[0]
    print(f"Alias name: {alias}")
    mydb = myc.connect(host='localhost', user='root', password='cosmos18', database='raw')
    cur = mydb.cursor()
    update_query = "UPDATE contacts SET phone_number = %s WHERE alias = %s"
    try:
        cur.execute(update_query, (new_phone_number, alias))
        mydb.commit()
        print(f'Phone number successfully updated for Alias name: {alias}')
    except Exception as e:
        print(f'Phone number update failed: {e}')
        mydb.rollback()
    finally:
        mydb.close()

def update_alias(old_alias: str, new_alias: str) -> None:
    '''update alias name from contacts'''
    list_aliases = get_all_aliases()
    if list_aliases==None:
        return
    alias_matches = match_word_func(old_alias, list_aliases)
    if not alias_matches:
        speak("No exact match found.")
        print("No exact match found.")
        return
    if len(alias_matches) == 1:
        old_alias = alias_matches[0]
    else:
        speak("I apologize, sir, but I am having difficulty determining the correct Alias name.")
        speak("Could you please inform me which one of the following options is the closest match?")
        speak("If none of the options matches, kindly specify 'none'.")
        print("Could you please inform me which one of the following options is the closest match?")
        print("If none of the options matches, kindly specify 'none'.")
        for i in alias_matches:
            print(f"Alias: {i}")
        alias_matches.append("none")
        check = commandeng()
        alias_matches = match_word_func(check, alias_matches)
        if "none" in alias_matches:
            speak("Apologies, sir. I couldn't determine the Alias name. We're terminating this query.")
            speak("Please double-check the alias name, and I'll provide a list for verification.")
            for i in list_aliases:
                print(i)
            return
        if len(alias_matches) != 1:
            speak("Apologies, sir. I couldn't determine the Alias name. We're terminating this query.")
            speak("Please double-check the alias name, and I'll provide a list for verification.")
            for i in list_aliases:
                print(i)
            return
        old_alias = alias_matches[0]
    print(f"Old Alias name: {old_alias}")
    print(f"New Alias name: {new_alias}")
    mydb = myc.connect(host='localhost', user='root', password='cosmos18', database='raw')
    cur = mydb.cursor()
    update_query = "UPDATE contacts SET alias = %s WHERE alias = %s"
    try:
        cur.execute(update_query, (new_alias, old_alias))
        mydb.commit()
        print(f'Alias name successfully updated from {old_alias} to {new_alias}')
    except myc.Error as e:
        print(f'Alias name update failed: {e}')
        mydb.rollback()
    finally:
        mydb.close()

def show_data_rci(rci: int) -> None:
    '''show all data of a particular RAW CORPORATE ID'''
    mydb = myc.connect(host='localhost', user='root', password='cosmos18', database='raw')
    cur = mydb.cursor()
    try:
        select_query = f"SELECT * FROM contacts WHERE contact_id={rci}"
        cur.execute(select_query)
        row = cur.fetchone()
        if not row:
            speak("RCI not found")
            print("RCI not found")
        else:
            print(f"RCI: {row[0]}\nFirst Name: {row[1]}\nLast Name: {row[2]}\nPhone Number: +{row[3]} {row[4]}\nAlias: {row[5]}")
            is_favorite = "Yes" if row[6] == 1 else "No"
            is_emergency_contact = "Yes" if row[7] == 1 else "No"
            print(f"Is Favorite: {is_favorite}  //  Is Emergency Contact: {is_emergency_contact}")
    except Exception as e:
        speak("An error occured.")
        print(f'Error fetching data: {e}')
    finally:
        mydb.close()

def show_whole_table() -> None:
    mydb = myc.connect(host='localhost', user='root', password='cosmos18', database='raw')
    cur = mydb.cursor()
    try:
        select_query = "SELECT * FROM contacts"
        cur.execute(select_query)
        rows = cur.fetchall()
        if not rows:
            speak("Empty contacts.")
            print("Empty contacts.")
        else:
            headers = ["RCI", "First name", "last name", "Country code", "Ph. No.", "Alias", "is_favorite", "is_emergency"]
            df = pd.DataFrame(rows, columns=headers)
            excel_file = 'H:\\AI\\raw_cosmos\\resource_files\\contacts_data.xlsx'
            df.to_excel(excel_file, index=False)
            speak("Opening excel sheet.")
            print("Opening excel sheet\n Loading...")
            os.system(excel_file)
    except Exception as e:
        speak("Error in fetching contacts.")
        print(f'Error fetching contacts: {e}')
    finally:
        mydb.close()

def update_contact_fav(alias: str,fav_ch: str) -> None:
    list_alias=get_all_aliases()
    if list_alias==None:
        return
    alias=match_word_func(alias,list_alias)
    if not alias:
        speak("No exact match found.")
        print("No exact match found.")
        return
    if len(alias)==1:
        alias=alias[0]
    else:
        speak("I apologize, sir, but I am having difficulty determining the correct Alias name.\nCould you please inform me which one of the following options is the closest match?\nIf none of the options matches, kindly specify 'none'.")
        for i in alias:
            print(f"Alias: {i}")
        alias.append("none")
        check=commandeng()
        alias=match_word_func(check,alias)
        if alias=="none":
            speak("Apologies, sir. I couldn't determine the Alias name. We're terminating this query.\nPlease double-check the alias name, and I'll provide a list for verification.")
            for i in list_alias:
                print(i)
            return
        if len(alias)!=1:
            speak("Apologies, sir. I couldn't determine the Alias name. We're terminating this query.\nPlease double-check the alias name, and I'll provide a list for verification.")
            for i in list_alias:
                print(i)
            return
        alias=alias[0]
    print(f"Alias name: {alias}")
    mydb = myc.connect(host='localhost', user='root', password='cosmos18', database='raw')
    cur = mydb.cursor()
    fav_ch=match_word_func(fav_ch,['yes','no'])
    if not fav_ch:
        speak("Sir can you please be more specific either 'yes' or 'no'." )
        speak("Enter yes or no")
        fav_ch=input("Enter yes or no: ")
        fav_ch=fav_ch.lower().strip()
        if fav_ch=='yes':
            speak("YES confirmed... proceeding.")
            print("YES confirmed... proceeding")
            fav_ch=1
        elif fav_ch=='no':
            speak("NO confirmed... proceeding.")
            print("NO confirmed... proceeding")
            fav_ch=0
        else:
            speak("Sorry sir only input yes or no is valid. Terminating query.")
            print("Query terminated.")
            return
    elif fav_ch=='yes':
        speak("YES confirmed... proceeding.")
        print("YES confirmed... proceeding")
        fav_ch=1
    elif fav_ch=='no':
        speak("NO confirmed... proceeding.")
        print("NO confirmed... proceeding")
        fav_ch=0
    else:
        speak("Sorry sir an error occured hence terminating query.")
        print('Error occured... terminating query')
        return
    update_query = "UPDATE contacts SET is_favorite = %s WHERE alias = %s"
    try:
        cur.execute(update_query, (fav_ch, alias))
        mydb.commit()
        speak(f'Favorite contacts successfully updated for {alias}')
        print(f'Favorite contacts successfully updated for Alias name: {alias}')
    except Exception as e:
        speak("Favorite contacts update failed due to below mentioned error.")
        print(f'Favorite contacts update failed: {e}')
        mydb.rollback()
    finally:
        mydb.close()

def update_contact_emergency(alias: str,em_ch: str) -> None:
    list_alias=get_all_aliases()
    if list_alias==None:
        return
    alias=match_word_func(alias,list_alias)
    if not alias:
        print("No exact match found.")
        speak("No exact match found.")
        return
    if len(alias)==1:
        alias=alias[0]
    else:
        speak("I apologize, sir, but I am having difficulty determining the correct Alias name.\nCould you please inform me which one of the following options is the closest match?\nIf none of the options matches, kindly specify 'none'.")
        for i in alias:
            print(f"Alias: {i}")
        alias.append("none")
        check=commandeng()
        alias=match_word_func(check,alias)
        if alias=="none":
            print("Apologies, sir. I couldn't determine the Alias name. We're terminating this query.\nPlease double-check the alias name, and I'll provide a list for verification.")
            for i in list_alias:
                print(i)
            return
        if len(alias)!=1:
            speak("Apologies, sir. I couldn't determine the Alias name. We're terminating this query.\nPlease double-check the alias name, and I'll provide a list for verification.")
            for i in list_alias:
                print(i)
            return
        alias=alias[0]
    print(f"Alias name: {alias}")
    mydb = myc.connect(host='localhost', user='root', password='cosmos18', database='raw')
    cur = mydb.cursor()
    em_ch=match_word_func(em_ch,['yes','no'])
    if not em_ch:
        speak("Sir can you please be more specific either 'yes' or 'no'." )
        speak("Enter yes or no")
        em_ch=input("Enter yes or no: ")
        em_ch=em_ch.lower().strip()
        if em_ch=='yes':
            speak("YES confirmed... proceeding.")
            print("YES confirmed... proceeding")
            em_ch=1
        elif em_ch=='no':
            speak("NO confirmed... proceeding.")
            print("NO confirmed... proceeding")
            em_ch=0
        else:
            speak("Sorry sir only input yes or no is valid. Terminating query.")
            print("Query terminated.")
            return
    elif em_ch=='yes':
        speak("YES confirmed... proceeding.")
        print("YES confirmed... proceeding")
        em_ch=1
    elif em_ch=='no':
        speak("NO confirmed... proceeding.")
        print("NO confirmed... proceeding")
        em_ch=0
    else:
        speak("Sorry sir an error occured hence terminating query.")
        print('Error occured... terminating query')
        return
    update_query = "UPDATE contacts SET is_emergency_contact = %s WHERE alias = %s"
    try:
        cur.execute(update_query, (em_ch, alias))
        mydb.commit()
        speak(f'Emergency contacts successfully updated for {alias}')
        print(f'Emergency contacts successfully updated for Alias name: {alias}')
    except Exception as e:
        speak("Emergency contacts update failed due to below mentioned error.")
        print(f'Emergency contacts update failed: {e}')
        mydb.rollback()
    finally:
        mydb.close()