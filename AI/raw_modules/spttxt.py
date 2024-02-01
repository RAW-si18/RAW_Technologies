# Updated 23/1/24

import speech_recognition as sr
import assemblyai as aai 
from raw_modules.speak_func import speak
aai.settings.api_key = "8bb9bcf61c2842c18f1b3f5d3eedcf76"

def commandeng(silent=False) -> str:
    '''understand command'''
    file_link=r"H:\AI\resource_files\spttxt.wav"
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    with microphone as source:
        try:
            if silent==False:
                speak("Listening...")
                print("Listening...")
            audio_data = recognizer.listen(source, timeout=3,  phrase_time_limit=10)
            with open(file_link, "wb") as file:
                file.write(audio_data.get_wav_data())
            if silent==False:
                print("Recognizing...")
            transcriber = aai.Transcriber()
            transcript = transcriber.transcribe(file_link)
            texts=transcript.text
            if silent==False:
                print("cc: ",transcript.text)
            texts=texts.lower()
        except sr.WaitTimeoutError:
            if silent==False:
                speak("My sincere apologies, sir. The system detected a timeout error.")
                print("My sincere apologies, sir. The system detected a timeout error.\nI'm actively addressing the issue to ensure a smoother experience.")
            texts="None"
        except sr.UnknownValueError:
            if silent==False:
                speak("Apologies, sir. I'm having trouble understanding your query.")
                print("Apologies, sir. I'm having trouble understanding your query.")
            texts="None"
        except sr.RequestError:
            if silent==False:
                speak("Unfortunately, we're experiencing a technical glitch, and as a result, the RAW spttxt server is currently unavailable.")
                print("Unfortunately, we're experiencing a technical glitch, and as a result, the RAW spttxt server is currently unavailable.")
            texts="None"
        except Exception as e:
            if silent==False:
                speak("Extremely sorry sir, something went wrong.")
                print("Error: ",e)
            texts="None"
    return texts