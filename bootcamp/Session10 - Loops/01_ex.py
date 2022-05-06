# Add up all odd numbers between 10 and 20
# Store the result in x:
x = 0

# YOUR CODE GOES HERE:
def odd_number():
    sumx = 0
    odds = range(11,21,2)
    for x in odds:
        print(x)
        sumx += x
    return sumx
        
x = odd_number()
print(x)