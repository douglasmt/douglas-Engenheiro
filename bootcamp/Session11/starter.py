import random

random_number = random.randint(1,10)  # numbers 1 - 10

# handle user guesses
#   if they guess correct, tell them they won
#     otherwise tell them if they are too high or too low

# BONUS - let player play again if they want!


def game():
    num = 0
    counter = 0
    while num != random_number:
        
        num = input("Guess a number between 1 and 10: ")
        counter += 1
        if int(num) == random_number:
            print("Congratulations! It was: " + str(num) + " in " + str(counter) + " attempts")
            break


game()

while input("Play again? (y/n)\n") != "n":
    random_number = random.randint(1,10)
    game()

