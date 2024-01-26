# Updated 26/1/24

from raw_modules.speak_func import speak
from raw_modules.spttxt import commandeng
from raw_modules.int_search import internet_search
from raw_modules.opening_app import openapp
from raw_modules.resume_cosmos import greet
from raw_modules.similar_sent import cosine_sent
from raw_modules.wikipedia_search import wikipedia
from raw_modules.similar_word import match_word_func
from raw_modules.set_alarm_func import set_alarm
import threading, re

def ch15_func(cmd: str) -> None:
    '''search on search engine'''
    speak("Search on Search engine activated.")
    print("Search on search engine")
    if 'google' in cmd:
        browser_name='google'
    elif 'bing' in cmd:
        browser_name='bing'
    elif 'brave' in cmd:
        browser_name='brave'
    else:
        browser_name=input("Preferred search engine: ")
    speak(f"What should i search on {browser_name}?")
    query=commandeng()
    if query=='None':
        return
    if 'incognito' in cmd:
        mode_search='incognito'
    else:
        mode_search='standard'
    internet_search(browser_name,query,mode_search)

def ch16_func() -> None:
    '''open app'''
    print("Open an app")
    app_name=commandeng()
    openapp(app_name)

def ch17_func() -> None:
    '''greet'''
    greet()

def ch18_func(cmd) -> None:
    '''alarm setup'''
    speak("Okay sir i will set an alarm for you")
    print("Alarm setup")
    speak("Enter hour in 12 hour format.")
    hr=int(input("Enter hour (12hr-format): "))
    mint=int(input("Enter minute: "))
    speak("Enter 0 for am and 1 for pm")
    ampm=int(input("Enter 0 for am and 1 for pm: "))
    if ampm==0:
        ampm='am'
    elif ampm==1:
        ampm='pm'
    else:
        speak("Only valid input is 0 or 1. Query terminated.")
        print("Query dismissed...")
        return
    purpose_pattern=r"alarm of\s*(.*)|alarm for\s*(.*)"
    purpose=re.findall(purpose_pattern,cmd)
    if purpose==None:
        purpose='reminder'
    alarm_thread = threading.Thread(target=set_alarm, args=(hr,mint,ampm,purpose))
    alarm_thread.start()

def ch19_func() -> None:
    '''similar sentence'''
    speak("Predicting best similar sentence based on logical sense!")
    print("Predict best logical similar from sentences")
    speak("Sir, what is the reference sentence for comparing with other sentences?")
    print("What is the reference sentence for comparing with other sentences?")
    t_sent=commandeng()
    if t_sent=='None':
        return
    speak("How many sentences do you have to compare which one best matches the reference sentence?")
    len_sent=int(input("Enter number of sentences: "))
    if len_sent<2:
        speak("Not enough sentences to compare with. Query Terminated.")
        print("Not enough sentences to compare. Query terminated.")
        return
    sent_list=[]
    for i in range(len_sent):
        sent=input(f"Enter sentence number {i+1}: ")
        sent_list.append(sent)
    best_match,match_per=cosine_sent(t_sent,sent_list)
    speak("Best matched sentence shown below.")
    print(f"Sentence: '{best_match}'\nmatches {match_per}%")
    speak(f"It matches {match_per}% with reference sentence.")

def ch20_func() -> None:
    '''spell wise similar'''
    speak("Predicting best similar words based on spell sense!")
    print("Predict best spell similar from words")
    speak("Sir, what is the reference words for comparing with other words?")
    print("What is the reference words for comparing with other words?")
    t_sent=input("Enter reference words: ")
    speak("How many words do you have to compare which one best matches the reference words?")
    len_sent=int(input("Enter number of words: "))
    if len_sent<2:
        speak("Not enough words to compare with. Query Terminated.")
        print("Not enough words to compare. Query terminated.")
        return
    words_list=[]
    for i in range(len_sent):
        wrd=input(f"Enter sentence number {i+1}: ")
        words_list.append(wrd)
    wrd_match=match_word_func(t_sent,words_list)
    if not wrd_match:
        speak("No exact matches found.")
        print("No exact matches found.")
        return
    if len(wrd_match)==1:
        speak("Best spell match indicated below.")
        print(f"Best spell match: {wrd_match[0]}")
    else:
        speak("I apologize, sir, but I am having difficulty determining the best word match.")
        j=1
        speak("Here are the most relevant spell matches.")
        print("Relevant matches: ")
        for i in wrd_match:
            print(f"{j}: {i}")
            j+=1
        
def ch21_func(cmd: str) -> None:
    '''wikipedia'''
    speak("Initiating Wikipedia search.")
    print("Wikipedia search initiated.")
    sum_list=['summary','short','brief','concise','compact','briefed','limited']
    detail_list=['complete','elaborate','detailed','full','thorough']
    input_list=[]
    summary,detail=0,0
    for word in cmd:
        input_list.append(word)
    for i in input_list:
        for j in (sum_list):
            if i==j:
                summary+=1
        for k in (detail_list):
            if i==k:
                detail+=1
    if summary>=detail:
        mode_ch='summary'
    else:
        mode_ch='text'
    print(f"MODE: {mode_ch}")
    speak("What specific topic are you interested in searching for on Wikipedia?")
    topic_query=commandeng()
    if topic_query=='None':
        speak("Enter the title you want to search for.")
        topic_query=input("Title: ")
    wikipedia(topic_query,mode_ch)