import random

options = ["rock", "paper", "scissors"]

def get_computer_choice():
    return random.choice(options)

def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "tie"
    elif (user_choice == "rock" and comp_choice == "scissors") or \
         (user_choice == "paper" and comp_choice == "rock") or \
         (user_choice == "scissors" and comp_choice == "paper"):
        return "user"
    else:
        return "comp"
