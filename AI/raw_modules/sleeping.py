# Updated 26/1/24

from raw_modules.spttxt import commandeng
from raw_modules.similar_sent import cosine_sent
from raw_modules.int_search import internet_search
from raw_modules.resume_cosmos import greet
from raw_modules.speak_func import speak
import pandas as pd
import time, re, csv

def sleeping() -> None:
    '''sleep mode detects keyword'''
    print("Sleep mode Activated !!")
    st_time=time.time()
    while True:
        command = commandeng(silent=True)
        if command == "None":
            continue
        if "cosmos" in command:
            end_time=time.time()
            if (end_time-st_time)>1800:
                greet()
            cmd_df = pd.read_csv(r'H:\AI\resource_files\data_study_cosmos.csv')
            index = len(cmd_df) + 1
            try:
                with open(r'H:\AI\resource_files\data_study_cosmos.csv', mode='a+', newline='') as cmd_file:
                    writer = csv.writer(cmd_file)
                    writer.writerows([[index,command]])
            except Exception as e:
                print(f"Error in data study: {e}")
            command = re.sub(r'^.*?\bcosmos\b\s*', '', command, count=1).strip()
            features = pd.read_csv(r"H:\AI\resource_files\features.csv")
            command_proper, match_perc = cosine_sent(command, features['features'])
            if (match_perc < 50) or ((features.loc[features["features"] == command_proper, 'index'].iloc[0])==0):
                speak("Hmmm... Yes, sir. I'm at your service. What would you like me to assist you with?")
                print("What would you like me to assist you with?")
                command = commandeng()
                if command == "None":
                    return [0,None]
                command_proper, match_perc = cosine_sent(command, features['features'])
                if match_perc >= 40:
                    ch_index = features.loc[features["features"] == command_proper, 'index'].iloc[0]
                    return [ch_index,command]
                else:
                    speak("I'm sorry, sir; I'm not familiar with that task. However, if you'd like, I can help by searching for it on Google. Would you like me to do that for you?")
                    check = commandeng()
                    check,_ = cosine_sent(check, ['yes', 'no'])
                    if check == 'yes':
                        internet_search("google", command, "normal")
                    else:
                        speak("Alright, sir. Closing this query for now. If you need further assistance, don't hesitate to call on Cosmos, I'm here for you.")
                        print("Query terminated...")
                    return [0,None]
            else:
                ch_index = features.loc[features["features"] == command_proper, 'index'].iloc[0]
                return [ch_index,command]
