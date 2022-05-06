sou2 = "super"
print(sou2[::-1]== sou2)

sou2 = "tacocat"
print(sou2[::-1]== sou2)
#'emevomer'

def is_palindrome(wor1):
    return wor1 == wor1[::-1]

print(is_palindrome("tacocat"))
print(is_palindrome("robert"))

def is_palindrome2(string):
    stripped = string.replace(" ", "")
    return stripped == stripped[::-1]

print(is_palindrome2("tac oca t"))
print(is_palindrome2("robe rt"))