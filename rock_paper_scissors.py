# We will write a rock paper scissors game in class - Complete it in this file

player_choice = "rock"
computer_choice = "paper"

# Create afunction that gets the choices
def get_choices():
    player_choice = "rock"
    computer_choice = "paper"
    choices = {"player": player_choice, "computer": computer_choice}

    return choices

choices = get_choices()
print(choices)