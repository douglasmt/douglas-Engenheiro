from random import randint  # use randint(a, b) to generate a random number between a and b

number = 0 # store random number in here, each time through
i = 0  # i should be incremented by one each iteration
number = randint(1,10)

while number != 5:
    number = randint(1,10)
    print("Try " + str(i) + " = " + str(number))
    i += 1

print("The times were " + str(i ))