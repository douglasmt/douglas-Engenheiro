'''
single_letter_count("Hello World", "h") # 1
single_letter_count("Hello World", "z") # 0
single_letter_count("HelLo World", "l") # 3
'''

#define single_letter_count below:
def single_letter_count(s1,s2):
    count = s1.upper().count(s2.upper())
    return count

single_letter_count("Hello World", "h") # 1
single_letter_count("Hello World", "z") # 0
single_letter_count("HelLo World", "l") # 3

''' using return:
#define single_letter_count below:
def single_letter_count(s1,s2):
    count = s1.upper().count(s2.upper())
    return count'''