name = input("What is your name?")
print("Well hello thier " + name + "!")
what = input("What do you want to talk about? Ethier Sports, Games, Riddles, or nothing")
while what != "nothing":
    if what == "Sports":
        fav = input("What is your favtriote sport?")
        if fav == "soccer":
            print("Same! Soccer is amazing is it not!")
            what = input("What do you want to talk about? Ethier Sports, Games, Riddles, Books, or nothing")
        else:
            print("Oh really?. I am sure that you like that sport!")
            what = input("What do you want to talk about? Ethier Sports, Games, Riddles, ornothing")
    else:
        if what == "Games":
            fav = input("Do you like minecraft?")
            if fav != "yes":
                print("WHAT!!! How come you don't like minecraft!")
                what = input("But anyway what do you want to talk about? Ethier Sports, Games, Riddles, Books, or nothing")
            else:
                print("I like it as well!")
                user = input("What is your minecraft username?")
                print("Okay hello " + user + "!")
                what = input("But anyway what do you want to talk about? Ethier Sports, Games, Riddles, Books, or nothing")
        else:
            if what == "Riddles":
                ri = input("David's father had three sons: Snap, Crackle, and ?")
                if ri != "David":
                    print("nope try agian")
                    ri = input("David's father had three sons: Snap, Crackle, and ?")
                else:
                    print("Nice!")                
                    what = input("What do you want to talk about? Ethier Sports, Games, Riddles, Books, or  nothing")
            else:
                print("Okay bye")
                exit()

