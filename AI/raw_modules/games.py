# Updated 23/1/24

import random
from raw_modules.speak_func import speak

def guess_number_game() -> None:
    '''guess a number game'''
    print("Mystic Number Quest")
    speak("Mystic Number Quest")
    print("The guidelines for this game are straightforward and easy to follow.")
    speak("The guidelines for this game are straightforward and easy to follow.")
    print("Sir, you have 5 opportunities. Successfully guess the right number, and you emerge as the victor!")
    speak("Sir, you have 5 opportunities. Successfully guess the right number, and you emerge as the victor!")
    ranum = random.randint(1,20)
    chance=1
    while chance<=5:
        guess = int(input("Take a shot at the mystery number, guess a digit between 1 and 20:"))
        if guess == ranum:
            speak("Congratulations! You've conquered the challenge and emerged victorious! Well done!")
            print("WON!!")
            break
        else:
            chance += 1
            speak("Oops, not quite there. The guessed number didn't match. Better luck on the next try!")
            print("WRONG GUESS")
    if not chance<=5:
        speak("Womp womp! The number wasn't in the mood to be found. Tough luck, but hey, laughter is the best consolation prize! ")
        print("LOSE!!")
        speak(f'The number was {ranum}')
        print(f'The number was {ranum}')
    speak('Your enjoyment is my success. Let the good times keep rolling, and feel free to dive into cosmos for any help')
