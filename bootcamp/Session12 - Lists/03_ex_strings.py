sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# Define your code below:
i = 0
result = ""
while i < len(sounds):
    result += str(sounds[i].upper())
    i += 1

print(result)