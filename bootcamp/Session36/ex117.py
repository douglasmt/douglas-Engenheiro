'''
truncate("Super cool", 2) # "Truncation must be at least 3 characters."
truncate("Super cool", 1) # "Truncation must be at least 3 characters."
truncate("Super cool", 0) # "Truncation must be at least 3 characters."
truncate("Hello World", 6) # "Hel..."
truncate("Problem solving is the best!", 10) # "Problem..."
truncate("Another test", 12) # "Another t..."
truncate("Woah", 4) # "W..."
truncate("Woah", 3) # "..."
truncate("Yo",100) # "Yo"
truncate("Holy guacamole!", 152) # "Holy guacamole!"

UDEMY
def truncate(string, n):
    if (n < 3):
        return "Truncation must be at least 3 characters."
    if (n > len(string) + 2):
        return string
 
    return string[:n - 3] + "..."
'''

def truncate(str_in, trunc_in):
    if trunc_in <= 2:
        return "Truncation must be at least 3 characters."
    else:
        if len(str_in) < trunc_in:
            return str_in[0:(trunc_in-3)]
        else:
            return str_in[0:(trunc_in-3)] + '...'


print(truncate("Super cool", 2)) # "Truncation must be at least 3 characters." OK
print(truncate("Super cool", 1)) # "Truncation must be at least 3 characters." OK
print(truncate("Super cool", 0)) # "Truncation must be at least 3 characters." OK
print(truncate("Hello World", 6)) # "Hel..." OK
print(truncate("Problem solving is the best!", 10)) # "Problem..." OK
print(truncate("Another test", 12)) # "Another t..." OK
print(truncate("Woah", 4)) # "W..." OK
print(truncate("Woah", 3)) # "..." OK
print(truncate("Yo",100)) # "Yo" OK
print(truncate("Holy guacamole!", 152)) # "Holy guacamole!"