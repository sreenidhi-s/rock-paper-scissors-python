import random
game_choice=["rock","paper","scissor"]
user_choice = input(str(print("enter your choice [rock or paper or scissors]")))
computer_choice = random.choice(game_choice)
if user_choice==computer_choice:
    print("it's a draw!")
elif user_choice=="rock" and computer_choice=="paper":
    print("you won!")
elif user_choice=="paper" and computer_choice=="rock":
    print("you lose :(")
elif user_choice=="paper" and computer_choice=="scissor":
    print("you lose :(")
elif user_choice=="scissor" and computer_choice=="paper":
    print("you won!")
elif user_choice=="rock" and computer_choice=="scissor":
    print("you lose")
elif user_choice=="scissor" and computer_choice=="rock":
    print("you won!")
else:
    print("your input was wrong :(")
