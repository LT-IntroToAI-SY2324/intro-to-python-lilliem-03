# We will write a rock paper scissors game in class - Complete it in this file
import random 

player_choice = "rock"
computer_choice = "paper"

# Create afunction that gets the choices
def get_choices():
    options = ["rock", "paper", "scissors"]
    player_choice = input("Enter a choice (rock, paper, or scissors)")
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}

    return choices

def check_win(player, computer):
    print(f"you chose {player}, computer chose {computer}")
    if player == computer:
        return "its a tie"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors, You Win!"
        else: 
            return "paper covers rock, You Lose!"

choices = get_choices()
print(choices)
result = check_win(choice["player"], choices ["computer"])
print (result)