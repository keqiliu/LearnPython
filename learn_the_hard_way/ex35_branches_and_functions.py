from sys import exit  # exit!! something new!!!

# exit(0) means a good exit
# exit(1) usually indicates there is an error


def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    how_much = 0
    try:
        how_much = int(choice)
    except ValueError:
        dead("Type in integer number please.")

    if how_much < 50:
        print("Nice, you are not greedy. You win!")
        exit(0)
    else:
        dead("You greedy dude!")


def bear_room():
    print("A bear here has a bunch of honey.")
    print("How are you going to move the bear?")
    bear_moved = False

    while 1:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear stares at you...Danger! Danger!")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off. Aiya...")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("Don't know that. Try something else?")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)


def start():
    print("You are in dark room.")
    print("Do you go to right or left?")

    choice = input("> ")

    if choice.lower() == "left":
        bear_room()
    elif choice.lower() == "right":
        cthulhu_room()
    else:
        dead("You stumble around until you starve.")


start()
