import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''


scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



print("Welcome to the Rock, Paper, Scissors game")

game_images = [rock, paper, scissors]

user_choice = int(input("Enter an integer: 0 for rock, 1 for paper, 2 for scissors!\n"))


if 0 <= user_choice <= 2:
    print("YOUR CHOICE")
    print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("COMPUTER'S CHOICE")

print(game_images[computer_choice])

if user_choice < 0 or user_choice >= 3:
    print("You entered an invalid number. YOU LOSE!")

elif user_choice == 0 and computer_choice == 2:
    print("YOU WIN!")

elif computer_choice == 0 and user_choice == 2:
    print("YOU LOSE!")

elif user_choice > computer_choice:
    print("YOU WIN!")

elif computer_choice > user_choice:
    print("YOU LOSE!")

else:
    print("IT'S A DRAW!")
