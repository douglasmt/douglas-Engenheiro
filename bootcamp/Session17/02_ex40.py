def yell(string_arg):
    message = string_arg.upper() + "!"
    return message
    
print(yell("Hello Jorge"))

# Using the string format() method:
'''
def yell(word):
    return "{}!".format(word.upper())
'''
# Using an f-string. My personal favorite, but only works in python 3.6 or later.  Udemy exercises don't support it currently :(
'''
def yell(word):
    return f"{word.upper()}!"

'''