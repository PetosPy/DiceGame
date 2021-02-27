import random
from Dice_game2 import logo
from replit import clear
print(logo)
print("Welcome to the game of Dice!")


game_not_exit = True
while game_not_exit:

    dice = random.randint(1,6)
    prompt = input("Type 'enter' to roll the dice for the first time or 'exit': ").lower()
    if prompt == "enter":
        first_time = dice
        print(f"Your first choice is number: {first_time}")

        dice_2 = random.randint(1,6)
        prompt_2 = input("Type 'enter' to roll the dice again or type 'exit': ").lower()
        if prompt_2 == "exit":
            game_not_exit = False
            print("good Bye and Thank you for checking out my game... love Michael")
        else:
            second_time = dice_2
            print(f"Your second choice is number: {second_time}")
            total = first_time + second_time
            print(f"You scored {total} points")

        continuation = input("Do you want to play again 'y' or 'n': ").lower()
        if continuation == "n":
            game_not_exit = False
        else:
            clear()
            print(logo)
            game_not_exit = True
    else:
        print("good Bye and Thank you for checking out my game... love Michael")
        game_not_exit = False
    



   