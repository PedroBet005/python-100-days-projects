print("Welcome to Treasure Island!")
print("Your mission is to find the hidden treasure!")

dilemma1 = input("You are at a crossroads. Where do you want to go: left or right?\n").lower()

if dilemma1 == "right":
    dilemma2 = input(
        'You have arrived at a lake. Type "wait" to wait for a boat or "swim" to swim across\n'
    ).lower()

    if dilemma2 == "wait":
        dilemma3 = input(
            "You arrive safely at the island. There are 3 doors: one red, one yellow, and one blue. Choose one\n"
        ).lower()

        if dilemma3 == "red":
            print("A guillotine has cut off your head. GAME OVER!")
        elif dilemma3 == "yellow":
            print("You found the treasure. You win!")
        elif dilemma3 == "blue":
            print("A bear trap has cut off your right leg. GAME OVER!")
        else:
            print("That door does not exist. GAME OVER!")
    else:
        print("A great white shark has ripped out your heart. GAME OVER!")
else:
    print("A Tyrannosaurus rex has stepped on you. GAME OVER!")

            