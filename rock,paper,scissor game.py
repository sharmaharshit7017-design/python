import random

options = {"rock", "paper", "scissors"}
playing = True

while playing:
    player = None
    computer = random.choice(list(options))  # Convert set to list for random.choice()
    
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()
    
    print(f"Player: {player}")
    print(f"Computer: {computer}")
    
    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You won!")
    elif player == "scissors" and computer == "rock":
        print("You lost!")
    elif player == "paper" and computer == "scissors":
        print("You lost!")
    elif player == "scissors" and computer == "paper":
        print("You won!")
    elif player == "rock" and computer == "paper":
        print("You lost!")
    elif player == "paper" and computer == "rock":
        print("You won!")
    
    play_again = input("Play again? (y/n): ").lower()
    if play_again != "y":  # Fixed: using != instead of incorrect assignment
        playing = False

print("Thanks for playing!")
