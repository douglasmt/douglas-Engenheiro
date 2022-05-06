def make_song(counter=99,beverage="soda"):
    i = counter
    while True:
        if i == 1:
            yield "Only 1 bottle of {} left!".format(beverage)
        elif i == 0:
            yield "No more {}!".format(beverage)
        elif i < 0:
            raise StopIteration
        else:
            yield "{} bottles of {} on the wall.".format(i,beverage)
        i -= 1


gen = make_song(5,"kombucha")
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

gen = make_song()
print(next(gen))
print(next(gen))


'''
UDEMY
Make Song Generator Solution
def make_song(verses=99, beverage="soda"):
    for num in range(verses, -1, -1):
        if num > 1:
            yield "{} bottles of {} on the wall.".format(num, beverage)
        elif num == 1:
            yield "Only 1 bottle of {} left!".format(beverage)
        else:
            yield "No more {}!".format(beverage)

'''