# I've made this game for fun. No I was neither high nor drunk. I've really just written anything that popped up in my head and saw in the
# process how it all fit together. And it's short
# It's just a warning




#Just definitions over here. There are literally three lines that were used for "activating" this game.

#There are three main functions: entry(), oldladyOption() and lyingDolphinOption()



#Inside those three options there are other options. These are here:

def didNotGiveUThisOptionOption():
    print("Did I give u this option? No. Please learn how to type")

def lieOption():
    print(">Never lie to an old lady!! AAAAAAAAYYA< *she throws a melon at your head. You are dead")
    entry()

def nameOption():
    answer = input(">Nice to meet you " + name + ", what can I do for you?<. She swings the melon in the direction of a child playing on the ground and misses their head for a few centimeters. She laughs. Type >mentor< or >bye< ").lower()
    if answer == "mentor":
        print("")
    
    elif answer == "bye":
        print("")
        entry()

    else:
        didNotGiveUThisOptionOption()
        nameOption()

#!!! Here we are 22.04.23. What does the old Lady do if you gave her your name and choose mentor or bye? 



def mentorAskingOption():
    print("You: >Can you be my mentor?<")
    print("Dolphin: >Why do you need a mentor?<")
    print("You: >Because every hero does<")
    print("Dolphin: >You are creating an uncomfortable atmosphere here... Why can't we just be good old friends?<")
    input("Type >friends< or >persist<: ").lower()

def friendOption():
    print("Dolphin: >Okay, I guess we're friends now<")
    print("... your task wasn't completed. You don't have a mentor. End of Adventure but Happy Ending? Take it as you like")
    print("END")

def persistOption():
    print("Dolphin: >So my first advice for you is: follow the sun son. And if there's no sun, follow the windflow. Go far far away from here and you'll arrive somewhere<")

def outsideVillageOption():
    print("Well, now you're outside the village. " + name + ", you jump on your horse again and we're ending this story right here. We all know what you will be doing won't we? You'll find yourself some monsters for you to do your best to gein their attention so they'll chase you and molest everyone around you. Thanks for playing this game! (It was all a joke, pls don't take it seriously) Bye!")



#Here I'm defining the start point event:

def entry():
    answer = input("You arrived at a village. You jump from your Spaghettimonster-Horse Nebula and go through the big ancient gate. You decide that you need a mentor to help and teach you. Choose between and old wrinkled >lady< that is throwing one watermelon after the other on those poor passing people on the market, or choose the flying >dolphin<. If you want to quit type >quit< ").lower()
    if answer == "lady":
        oldLadyOption()
    
    elif answer == "dolphin":
        flyingDoplhinOption()

    elif answer == "quit":
        quit()

    else: 
        didNotGiveUThisOptionOption()



#Here are the two other main paths:

def oldLadyOption():
    print("She is holding another melon, aiming for a man with a hiking stick, but now she's lowering her right arm when she sees that you are staring at her.")
    print("Old Lady: >Don't you have something else to do instead of bothering an old lady? What's your name anyway?<.")
    answer = input("You can >lie< or tell her your >name<: ").lower()

    if answer == "lie":
        lieOption()
    
    elif answer == "name":
        nameOption()
        flyingDoplhinOption()

    else:
        didNotGiveUThisOptionOption()
        oldLadyOption()



def flyingDoplhinOption():
    print("The flying Dolphin is actually not flying but sitting on the oak gate stalking all the people around the village's market. He has sunglasses on, although the sun is nearly touching the ground, which causes the shadows to be long and bordered by orange and pink light. You climb the ladder that was put there. And while you place hand after hand on the wooden sticks you ask yourself why there's a ladder if no one else than a flying Dolphin likes sitting on this place? It's actually forbidden to do so in the village's law, but the Dolphin is, well, a Dolphin and doesn't count as >person<, so the rules don't apply to him. He's basically their god.")
    answer = input("You are now at the top. You sit next to the Dolphin. Type >mentor< or >starting point<: ").lower()

    if answer == "mentor":
        mentorAskingOption()

        if answer == "persist":
            persistOption()
            mentorAskingOption()

        elif answer == "friends":
            friendOption()
            entry()

        else:
            didNotGiveUThisOptionOption()
            flyingDoplhinOption()
    
    elif answer == "starting point":
        entry()

    else:
        didNotGiveUThisOptionOption()
        flyingDoplhinOption()



#The actual starting point is here
name = input("Type your name: ")
print("Welcome", name, "to this adventure!")
entry()



#It's not ready
#Sources: https://www.youtube.com/watch?v=DLn3jOsNRVE&list=PLsCTnBEpCwH-MZja6wejVZ6sdMbghuGYd&index=6&t=3400s
#Date: 16.04.2023