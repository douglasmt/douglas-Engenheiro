print("Rock...")
print("Paper...")
print("Scissors...")
print("-" * 20)

player1 = input("Player 1, make your move: ")
player2 = input("Player 2, make your move: ")
print("-" * 20)

if player1 == "rock" and player2 == "scissors":
	print("player 1 wins!")
elif player1 == "rock" and player2 == "paper":
	print("player 2 wins!")
elif player1 == "paper" and player2 == "rock":
	print("player 1 wins!")
elif player1 == "paper" and player2 == "scissors":
	print("player 2 wins!")
elif player1 == "scissors" and player2 == "rock":
	print("player 2 wins!")
elif player1 == "scissors" and player2 == "paper":
	print("player 1 wins!")
elif player1 == player2:
	print("It's a tie!")
else:
	print("something went wrong")