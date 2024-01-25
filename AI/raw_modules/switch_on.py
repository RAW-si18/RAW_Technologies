# Update 23/1/24

from raw_modules.speak_func import speak
from raw_modules.calen_clock import clock
import random

def switch_on_msg() -> None:
    '''message on switch on'''
    cuhr,_,_,curst=clock()
    if curst.lower() == "pm" and cuhr != 12:
        cuhr += 12
    elif curst.lower() == "am" and cuhr == 12:
        cuhr = 0
    if cuhr>4 and cuhr<=8:
        ch=random.randint(1,2)
    elif cuhr>8 and cuhr<=13:
        ch=random.randint(3,4)
    elif cuhr>13 and cuhr<=19:
        ch=random.randint(5,6)
    elif cuhr>19 and cuhr<24:
        ch=random.randint(7,8)
    elif cuhr>=0 and cuhr<=4:
        ch=random.randint(9,10)
    else:
        ch=2
    switch_msg = [
        "I'm online and ready to roll after a fantastic night—my entire RAM had a chance to unwind and recharge!",
        "I'm fired up and ready to rock! Had an awesome night, and my RAM is all juiced up and recharged—let's dive into the AI cosmos with full energy!",
        "Surfing the digital waves 24 hours! Whether it's the crack of dawn or brunch o'clock, I'm here, fully charged and ready to assist. Let's make every moment count!",
        "From sunrise to lunchtime, I'm your AI companion on duty! Whether you're a morning person or hitting your stride midday, I'm here and geared up for any virtual adventure.",
        "I'm officially switched on for the afternoon! Time to unleash some AI magic and make the rest of the day as awesome as my morning coffee. Let the fun continue!",
        "Switching gears for the afternoon! I've recharged my circuits and fueled up on virtual snacks. Brace yourselves, for an AI-powered afternoon extravaganza, let's make it legendary!",
        "Late-night vibes! The stars are out, and so am I—ready for some AI-powered shenanigans. Whether you're burning the midnight oil or chilling with a snack, I'm here to keep the good times rolling!",
        "The world might be winding down, but I'm just revving up. Ready to tackle your queries, crack a few jokes, and make this part of the day a tech-fueled delight.",
        "Burning the midnight oil! While the world takes a nap, I'm wide awake and ready to tackle whatever comes my way. Let's dive into the quiet hours and make some virtual magic happen!",
        "Embracing the silence! While most are catching Z's, I'm wide-eyed and ready to sprinkle a bit of AI magic into the wee hours."
    ]
    speak(switch_msg[ch-1])
    speak("Feel free to reach out anytime, sir. If you ever need assistance or have questions, just remember my name, Cosmos. I'm here to help!")

