name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You arrived at a village. You jump from your Spaghettimonster-Horse Nebula and go through the big ancient gate. You decide that you need a mentor to help and teach you. Choose between and old wrinkled lady that is throwing one watermelon after the other on the passing people on the market, or choose the flying dolphin ").lower()

if answer == "wrinkled lady":
    answer = input("She is holding another melon, aiming for a man with a hiking stick, but lower her right arm when she sees that you are staring at her. >Don't you have something else to do instead of bothering an old lady? What's your name anyway?<. You can >lie< or tell her your >name< ").lower()

    if answer == "lie":
        print(">Never lie to an old lady!! AAAAAAAAYYA< *she throws a melon at your head. You are dead")
    
    elif answer == "name":
        print(">Nice to meet you", name, ", what can I do for you?<. She swings the melon in the direction of a child playing on the ground and misses their had for a few centimeters. She laughs. Type >mentor< or >Have a nice day<")
        if answer == "mentor":
            print(">Why? Are you out of your mind? But yeah, this makes sense. I'm too. People attract people that they are similar too. Or was it the other way around? But I'm not interested. Go to mister Dolphin")
        
        elif answer == "have a nice day":
            print(">You too honey! If you see some damaged people walking around. It's because of me")

    else:
        input(">I can't understand what you're mumbling. Speak or shut up forever<. ")
        if answer == ""

elif answer == "flying dolphin":
    print()
else:
    print("Did I give u this option? No. Please learn to type")