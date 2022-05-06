# Define combine_words below:
def combine_words(word,**kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']    
    return word

print(combine_words("child"))
print(combine_words("child", prefix="man"))
print(combine_words("child", sufix="ish"))
print(combine_words("work", sufix="er"))
''' I copied the solution here, with the same code as mine, and worked when I pasted in udemy.
def combine_words(word,**kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word
'''