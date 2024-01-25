# Updated 23/1/24

import re
from raw_modules.speak_func import speak

def extract_email(filelink: str) -> None:
    '''extract email id from a file'''
    resnum=0
    filelink=filelink.replace('"', '')
    with open(filelink,"r") as mf:
        extpara=mf.read()   
        email_pattern=r"([a-zA-Z\.0-9\_]+@[A-Za-z]+\.[A-Za-z\.]+)"
        result=re.findall(email_pattern,extpara)
        for i in result:
            resnum+=1
        speak("Number of results Found: ",resnum)
        print("Results Found: ",resnum)
        for i in range(resnum):
            print(result[i])

def extract_phone(filelink: str) -> None:
    '''extract phone number from a file'''
    resnum=0
    filelink=filelink.replace('"', '')
    with open(filelink,"r") as mf:
        extpara=mf.read()   
        phonelist=[]
        ph_pattern1=r"(\+[0-9]* [0-9]{10}\b)"
        ph_pattern2=r"([0-9]{3}\.[0-9]{3}\.[0-9]{4})"
        ph_pattern3=r"([0-9]{3}\-[0-9]{3}\-[0-9]{4})"
        ph_pattern4=r"(\([0-9]{3}\) [0-9]{3}\-[0-9]{4})"
        ph_pattern5=r"(\b[0-9]{10}\b)"
        ph_pattern6=r"(\+[0-9]* [0-9]{3} [0-9]{3} [0-9]{4})"
        pattern=[ph_pattern1,ph_pattern2,ph_pattern3,ph_pattern4,ph_pattern5,ph_pattern6]
        for i in range(6):
            match_phone=re.findall(pattern[i],extpara)
            for j in match_phone:
                phonelist.append(j)
                resnum+=1
        speak(f"{resnum} Result found.")
        print(f"{resnum} Result found: ")
        for i in range(resnum):
            print(phonelist[i])

def extract_humdata(filelink: str) -> None:
    '''extract phone human data from a file'''
    resnum=0
    filelink=filelink.replace('"', '')
    with open(filelink,"r") as mf:
        extpara=mf.read()
        match_name=re.findall(r"Born\s([a-zA-Z]*\s[a-zA-Z]*\s[a-zA-Z]*\b)",extpara)
        match_age=re.findall(r"\(age (\d+)\)",extpara)
        match_bdate=re.findall(r'Born.*\n(.*)\(age', extpara)
        match_place=re.findall(r'\(age.*\n(.*)',extpara)
        for i in match_name:
            resnum+=1
        speak(f"{resnum} results found.")
        print("Results Found: ",resnum)
        for i in range(resnum):
            print('')
            print('Name: ',match_name[i].strip())
            print('Age: ',match_age[i].strip())
            print("Birth Date: ",match_bdate[i].strip())
            print("Birth Place: ",match_place[i].strip())