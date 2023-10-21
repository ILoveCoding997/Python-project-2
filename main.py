# Rock Paper Scissors Game!
import random

options = ['Rock', 'Paper', 'Scissors']
computer = random.choice(options)
player = input("Enter a choice(Rock, paper, scissors): ")
print(f"Player: {player}")
print(f"Computer: {computer}")

if player == "rock" and computer == "Paper":
    print("Computer Wins!")
if player == "paper" and computer == "Scissors":
    print("Computer Wins!")
if player == "scissors" and computer == "Rock":
    print("Computer Wins!")
if player == "rock" and computer == "Rock":
    print("Its a draw!")
if player == "paper" and computer == "Paper":
    print("Its a draw!")
if player == "scissors" and computer == "Scissors":
    print("Its a draw!")
if player == "rock" and computer == "Scissors":
    print("You win!")
if player == "paper" and computer == "Rock":
    print("You win!")
if player == "scissors" and computer == "Paper":
    print("You win!")
