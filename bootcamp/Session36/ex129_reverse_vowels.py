'''
reverse_vowels("Hello!") # "Holle!" 
reverse_vowels("Tomatoes") # "Temotaos" 
reverse_vowels("Reverse Vowels In A String") # "RivArsI Vewols en e Streng"
reverse_vowels("aeiou") # "uoiea"
reverse_vowels("why try, shy fly?") # "why try, shy fly?"

UDEMY
def reverse_vowels(s):
    vowels = "aeiou"
    string = list(s) # transform s in a list
    i, j = 0, len(s) - 1
    while i < j:
        if string[i].lower() not in vowels: # if letter from s(string) is in vowels
            i += 1                          # following letter in s
        elif string[j].lower() not in vowels: 
            j -= 1
        else:
            string[i], string[j] = string[j], string[i] # reversing the values
            i += 1
            j -= 1
    return "".join(string)
'''

# def reverse_vowels(text_in):
#     vow_ord = []
#     vow_list = []
#     for i in range(0,len(text_in)):
#         if text_in[i].lower() in 'aeiou':
#             vow_ord.append(i)
#             vow_list.append(text_in[i])
#     rev_vowels = vow_list[::-1]
#     print(vow_ord)
#     print(vow_list)
#     print(rev_vowels)
#     text_out = list()
#     for i in range(0,len(rev_vowels)):
#         text_in[i] = text_in[i]
#             print(text_out[i])
#         else:
#             text_out[i] = rev_vowels[i]



#     return text_out
def reverse_vowels(s):
    vowels = "aeiou"
    string = list(s) # transform s in a list
    i, j = 0, len(s) - 1
    while i < j:
        if string[i].lower() not in vowels: # if letter from s(string) is in vowels
            print("i não está nas vogais. {} ".format(string[i].lower()))
            i += 1                          # following letter in s
        elif string[j].lower() not in vowels: 
            print("j não está nas vogais. {} ".format(string[j].lower()))
            j -= 1
        else:
            print(string)
            string[i], string[j] = string[j], string[i] # reversing the values
            i += 1
            j -= 1
    return "".join(string)
print(reverse_vowels("Hello!") )
print(reverse_vowels("aeiou"))
print(reverse_vowels("Reverse Vowels In A String"))
print(reverse_vowels("aeiou"))
print(reverse_vowels("why try, shy fly?") )