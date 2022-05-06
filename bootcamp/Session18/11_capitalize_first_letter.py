'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''

def capitalize(name1):
    return name1[0].upper() + name1[1:]
    # Another option: return name1[:1].upper() + name1[1:]

print(capitalize("tim")) # "Tim"
print(capitalize("matt")) # "Matt")    