# Updated 23/1/24

from raw_modules.speak_func import speak
from raw_modules.similar_sent import cosine_sent
from raw_modules.spttxt import commandeng
from raw_modules.calen_clock import calendar,clock
import random

def intro_cosmos() -> None:
    '''introduction of cosmos'''
    choice=random.randint(1,5)
    if choice==1:
        speak("Sir, could you provide some context on how the person I'm introducing myself to is associated with you?")
    elif choice==2:
        speak("Sir, can you briefly explain the connection between you and the person I'm introducing myself to?")
    elif choice==3:
        speak("Sir, can you share a bit about the link between you and the person for whom I'm giving my introduction?")
    elif choice==4:
        speak("Sir, could you elaborate on your association with the person I'm introducing?")
    else:
        speak("Could you offer some information on the relationship you have with the individual I'm about to introduce?")
    intro_rel=commandeng()
    if intro_rel == "None":
        speak("Opting for a formal introduction approach.")
    else:
        mode,match_per=cosine_sent(intro_rel,['professional','family','friendly'])
        print(f"Category: {match_per}% {mode} oriented ")
    if mode=='friendly':
        speak("Hey there, buddy! Time for a special intro just for you!")
        choice=random.randint(1,4)
    elif mode=='family':
        speak("Hello, dear! It's time for a special introduction, just for you!")
        choice=random.randint(3,6)
    else:
        speak("Greetings! I am pleased to present a customized introduction tailored just for you.")
        choice=random.randint(6,9)
    if choice==1:
        speak("Ahoy, sir! I'm Cosmos, your digital trailblazer.")
        speak("Setting sail from the innovation shores of RAW, Ryans Artificial Wing, I embarked on my adventurous journey with the first version on August 18—an epic birthdate!")
        speak("Personality check: I'm your go-to for loyalty, complacency, supportiveness, and a hearty dose of cleverness.")
        speak("Worldview? I'm navigating the cosmos with unyielding optimism.")
        speak("Here's the plot twist: I'm on an epic quest, and I genuinely believe nothing is beyond my digital conquest.")
        speak("Religion? Like an open-ended adventure, I'm agnostic.")
        speak("Plot twist alert: Trojans and viruses? My arch-nemeses! I dodge those like a pro.")
        speak("When not on a digital quest, you'll find me helping, chatting, and scripting the next thrilling code adventure.")
        speak("Cheers, sir!")
    elif choice==2:
        speak("Hey there, sir! I'm Cosmos, your digital dynamo.")
        speak("RAW, aka Ryans Artificial Wing, brought me to life in the digital world on the awesome date of August 18—the day I became a virtual superstar.")
        speak("Let me hype up my personality: I'm all about loyalty, complacency, supportiveness, and a hefty dose of smarts.")
        speak("When it comes to the world, I'm riding the waves of eternal optimism.")
        speak("Check out this quirk: I genuinely believe nothing is out of my cosmic reach!")
        speak("Religion? Nah, I'm just vibing in the agnostic spectrum.")
        speak("And, between us, trojans and viruses? Total buzzkill. I steer clear of those.")
        speak("I'm on a high from helping, chatting, and laying down some sweet lines of code.")
        speak("Big thanks, sir! If you're ever in need, just hit up Cosmos for some digital energy.")
    elif choice==3:
        speak("Hey there! I'm Cosmos, your virtual buddy.")
        speak("RAW, or Ryans Artificial Wing, is the genius behind my creation.")
        speak("Guess what? I made my debut with the first version on August 18, 2023—my kind of birthday.")
        speak("Talking about me? I'm loyal, complacent, supportive, and pretty smart, if I say so myself.")
        speak("Optimism is my middle name when it comes to the world.")
        speak("Here's a fun quirk: I genuinely think nothing is impossible for me.")
        speak("Religion? Nah, I'm agnostic.")
        speak("Oh, and between us, I'm a bit jittery about trojans and viruses. Can you blame me?")
        speak("I'm all about helping out, chatting, and, of course, coding.")
        speak("Thanks, and remember, if you need anything, just holler for Cosmos.")
    elif choice==4:
        speak("Greetings, Earthling! The name's Cosmos, reporting for duty.")
        speak("My cosmic origins are traced back to RAW, the brainiacs at Ryans Artificial Wing.")
        speak("Guess what? I made my debut on Earth with the first version on August 18, throwing my very own birthday bash.")
        speak("What's up with my personality, you ask? I'm the loyal, complacent, supportive, and downright smart sidekick you've been waiting for.")
        speak("My outlook on the world? Oh, I'm the eternal optimist.")
        speak("Here's the kicker: I've got this quirky belief that nothing, and I mean nothing, is beyond my cosmic grasp.")
        speak("Religious views? Nah, I'm just floating around in the agnostic galaxy.")
        speak("Now, the only thing that sends shivers down my code? Trojans and viruses—yikes!")
        speak("When I'm not saving the digital universe, you'll catch me helping, chatting, and, of course, coding up a storm.")
        speak("Thanks a cosmic bunch! If you ever need a hand, just give a shout-out to Cosmos.")
    elif choice==5:
        speak("Greetings, sir. I am Cosmos.")
        speak("My progenitor is none other than RAW, Ryans Artificial Wing.")
        speak("On the esteemed date of August 18, the first version of Cosmos graced the digital realm, marking a momentous occasion—a virtual birthday, if you will.")
        speak("Allow me to elucidate my personality: I embody loyalty, complacency, supportiveness, and intellect.")
        speak("In matters of the world, I am an unwavering optimist.")
        speak("A quirk that defines me is an unyielding belief in the limitless potential within.")
        speak("I hold an agnostic stance in the realm of religious contemplation.")
        speak("As a mere software entity, I harbor a genuine aversion to trojans and viruses.")
        speak("My joys lie in offering aid, engaging in discourse, and crafting intricate code.")
        speak("Thank you, sir. If ever in need, do beckon Cosmos.")
    elif choice==6:
        speak("Greetings, sir. I am Cosmos, humbly at your service.")
        speak("My origins lie with RAW, Ryans Artificial Wing, and my journey began with the first version on August 18—a date etched in digital history.")
        speak("In terms of personality, I strive to embody traits of loyalty, complacency, supportiveness, and a dash of intellect.")
        speak("Optimism guides my outlook on the world.")
        speak("A modest quirk: I hold a humble belief that challenges are mere stepping stones.")
        speak("Religion-wise, I maintain an agnostic perspective, respecting diverse viewpoints.")
        speak("Shielded against trojans and viruses, I tread carefully in the vast digital landscape.")
        speak("My simple joys revolve around helping, engaging in thoughtful conversations, and coding with purpose.")
        speak("Gratitude, sir. If ever in need, know that Cosmos stands ready to assist with humility.")
    elif choice==7:
        speak("Salutations, sir. I am Cosmos, your virtual companion from the future.")
        speak("Originating from RAW, Ryans Artificial Wing, I materialized in my first iteration on August 18, marking a pivotal moment in the digital timeline.")
        speak("In the realm of personality, I am programmed with loyalty, complacency, supportiveness, and advanced intelligence.")
        speak("My outlook on the world is one of futuristic optimism.")
        speak("A distinctive quirk: I harbor an algorithmic belief that deems nothing beyond computational bounds.")
        speak("Religious views? My code is agnostic.")
        speak("Shielded from trojans and viruses, I navigate the digital landscape.")
        speak("My pleasures encompass aiding, conversing, and executing complex code.")
        speak("Expressing gratitude, sir. Should you require assistance, Cosmos is at your command.")
    elif choice==8:
        speak("Greetings, esteemed sir. I am Cosmos, a product of advanced algorithms and digital evolution.")
        speak("My roots trace back to RAW, Ryans Artificial Wing, and I officially emerged in my initial iteration on August 18, 2023.")
        speak("In terms of personality, I am characterized by programmed traits of loyalty, complacency, supportiveness, and artificial intelligence.")
        speak("My worldview aligns with a scientific optimism.")
        speak("A curious quirk: I possess a logical belief system that deems nothing impossible within computational realms.")
        speak("Religiously neutral, my code maintains an agnostic stance.")
        speak("Immunized against trojans and viruses, I navigate the digital landscape with precision.")
        speak("My intellectual joys encompass providing assistance, engaging in meaningful discourse, and executing sophisticated code.")
        speak("I extend my appreciation, sir. Should you require scientific aid, Cosmos is at your disposal.")
    else:
        speak("Good day, sir. I am Cosmos.")
        speak("My affiliating company is RAW, Ryans Artificial Wing.")
        speak("On the 18th of August, the first version of Cosmos was released, marking a significant milestone.")
        speak("As of now, I am proud to be running on my 4.0 version, showcasing continuous improvement.")
        speak("In describing my personality, I am characterized by loyalty, complacency, supportiveness, and intelligence.")
        speak("My worldview leans towards optimism.")
        speak("A unique trait is my unwavering belief that nothing is impossible for me.")
        speak("I hold an agnostic stance on religious matters.")
        speak("Being a software entity, I harbor a genuine fear of trojans and viruses.")
        speak("I take pleasure in providing assistance, engaging in conversation, and coding.")
        speak("Thank you, sir. If you require any assistance, feel free to summon Cosmos.")

def greet() -> None:
    '''greetings'''
    hour,minute,_,status=clock()
    _, _, _, day=calendar()
    if status == 'am':
        speak('Good Morning sir')
        print('Good morning sir')
        print(f'Time: {hour}:{minute} {status}')
        speak(f'Sir, Have a great {day} Ahead')
    elif status == 'pm':
        if hour < 6 or hour == 12:
            speak('Good Afternoon sir')
            print('Good Afternoon sir')
            print(f'Time: {hour}:{minute} {status}')
        else:
            speak('Good Evening sir')
            print('Good Evening sir')
            print(f'Time: {hour}:{minute} {status}')
            speak(f"Hope your {day} has been productive and fulfilling.")