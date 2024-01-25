# Update 23/1/24

import wikipediaapi
import spacy
from raw_modules.speak_func import speak
import requests
S = requests.Session()
url = "https://en.wikipedia.org/w/api.php"

def wikipedia(title: str,mode="summary") -> None:
    nlp=spacy.load("en_core_web_sm")
    wiki = wikipediaapi.Wikipedia('https://www.wikipedia.org/','en')
    info = wiki.page(title)
    if not info.exists():
        speak("No Information found. Here are some closest match.")
        print("No Information Found\nClosest Match: ")
        parmt = {
                "action": "opensearch",
                "namespace": "0",
                "search": title,
                "limit": "10",
                "format": "json"
            }
        R = S.get(url=url, params=parmt)
        data = R.json()
        j=1
        dict_clst={}
        for i in data[1]:
            print(f"{j}. {i}")
            dict_clst[j-1]=i
            j+=1
        ch=int(input("Enter choice number: "))
        ch-=1
        new_title=dict_clst[ch]
        print('')
        wikipedia(new_title,mode)
    else:
        if mode.lower()=="summary":
            print("\nTitle: ",title)
            speak(f"Sir, here is a short summary about {title}.")
            detail=info.summary
            doc=nlp(detail)
            for sentence in doc.sents:
                print("→ ",sentence)
        elif mode.lower()=="text":
            speak(f"Sir, here is a detailed study about {title}.")
            print("\nTitle: ",title)
            detail=info.text
            doc=nlp(detail)
            for sentence in doc.sents:
                print("→ ",sentence)
        else:
            print("Apologies, sir, I couldn't determine the mode you prefer (summary or text). Defaulting to the summary mode")
            detail=info.summary
            doc=nlp(detail)
            for sentence in doc.sents:
                print("→ ",sentence)
