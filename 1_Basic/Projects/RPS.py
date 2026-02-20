import random

def get_choices():
    player_choice=input("Enter a choice(rock,paper,scissors): ")
    options=["rock","paper","scissors"]
    computer_choice=random.choice(options)
    print(f"computer choice: {computer_choice}")
    choices={"player":player_choice,"computer":computer_choice}
    return choices

def check_win(player,computer):
    if player==computer:
        return "its a tie!"

    elif player=="rock":
        if computer=="scissors" :
            return "rock smashes scissors! you win!"
        else:
            return "paper covers rock! you lose!"
    
    elif player=="paper":
        if computer=="rock" :
            return "paper covers rock! you win!"
        else:
            return "scissors cuts paper! you lose!"

    elif player=="scissors":
        if computer=="rock" :
            return "rock smashes scissors! you lose!"
        else:
            return "scissors cuts paper! you win!"

choices=get_choices()
result=check_win(choices["player"],choices["computer"])

print(result)