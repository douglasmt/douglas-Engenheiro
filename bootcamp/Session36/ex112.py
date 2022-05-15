'''
vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}

UDEMY
def vowel_count(string):
    lower_s = string.lower()
    return {letter: lower_s.count(letter) for letter in lower_s if letter in "aeiou"}
'''

def vowel_count(word):
    vowels_lower = word.lower()
    vowels = { l:vowels_lower.count(l) for l in vowels_lower if l in 'aeiou' }    

    return vowels

print(vowel_count('awesome'))
print(vowel_count('Elie'))
print(vowel_count('Colt'))
