def yes_or_no():
    answer = ["yes","no"]
    i = 0
    while True:
        if i >= len(answer): i = 0
        yield answer[i]
        i += 1


gen = yes_or_no()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))