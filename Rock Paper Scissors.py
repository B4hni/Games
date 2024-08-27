# ROCK PAPER SCISSORS GAME

from random import choice

# Create a list of play options
t = ["Rock", "Paper", "Scissors"]

# Function to determine the winner
def determine_winner(player, computer):
    if player == computer:
        return "Tie!"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return f"You win! {player} beats {computer}"
    else:
        return f"You lose! {computer} beats {player}"

while True:
    # Get player's input and validate it
    player = input("Rock, Paper, Scissors? ").capitalize()
    if player not in t:
        print("That's not a valid play. Check your spelling!")
        continue
    
    # Assign a random play to the computer
    computer = choice(t)
    
    # Determine the winner and print the result
    result = determine_winner(player, computer)
    print(result)
    
    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
