# Updated 31/1/24

import mysql.connector
import random
import time
from raw_modules.speak_func import speak

def get_joke() -> None:
    '''jokes by raw'''
    speak("Let me entertain you with my joke.")
    mysql_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'cosmos18',
        'database': 'raw'
    }
    joke_number=random.randint(1,38269)
    conn = mysql.connector.connect(**mysql_config)
    cursor = conn.cursor()
    select_query = "SELECT question_joke, answer_joke FROM q_a_jokes WHERE joke_number = %s"
    cursor.execute(select_query, (joke_number,))
    joke_data = cursor.fetchone()
    cursor.close()
    conn.close()
    if joke_data:
        question, answer = joke_data
        print("Question:", question)
        speak(question)
        time.sleep(3)
        speak(answer)
        print("Answer:", answer)
    else:
        speak("I'm terribly sorry, sir, but it seems I'm not quite in the mood to narrate a joke at the moment. Perhaps another time?")
