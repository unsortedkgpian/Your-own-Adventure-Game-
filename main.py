answer = input("What you like to play? (yes/no) ")

if answer.lower().strip() == "yes":

    answer = input("You reach a crossroads, would you like to left or right").lower().strip()
    if answer == "left":
        answer = input("You encounter a monster, would you like to run or attack.").lower().strip()

        if answer == "attack":
            print("You mindless fool. You are Dead!")
        else:
            print("Big brain Moment!, Bach gya nice")

    elif answer == "right":
        answer = input("You have encounter a 8 week hungry lion would you like to run or attack.").lower().strip()
        if answer == "attack":
            print("big brain moment")
            answer = input("You have encounter a 1000 old man You want to talk or move forward").lower().strip()
            if answer == "talk":
                print("You got brain with no use 1000 old man is boss of the cave you lost!")
            else:
                print("You won")
        else:
            print("You fool he's dead still you ran you lost!")

    else:
        print("Invalid choice, you lost!")

else:
    print("That's to bad Please try this one time!")