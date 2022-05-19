'''
reverse_vowels("Hello!") # "Holle!" 
reverse_vowels("Tomatoes") # "Temotaos" 
reverse_vowels("Reverse Vowels In A String") # "RivArsI Vewols en e Streng"
reverse_vowels("aeiou") # "uoiea"
reverse_vowels("why try, shy fly?") # "why try, shy fly?"
'''

def reverse_vowels(text_in):
    vow_ord = []
    vow_list = []
    for i in range(0,len(text_in)):
        if text_in[i].lower() in 'aeiou':
            vow_ord.append(i)
            vow_list.append(text_in[i])
    rev_vowels = vow_list[::-1]
    print(vow_ord)
    print(vow_list)
    print(rev_vowels)
    text_out = str()
    for i in len(text_in):
        if text_in[i] not in vow_ord:
            text_out[i] = text_in[i]
        else:
                



    for j in range(len(vow_ord)):
        print(vow_ord[j])
        print(text_in[vow_ord[j]])# = rev_vowels[vow_ord[j]]
    return text_in

print(reverse_vowels("Hello!") )
print(reverse_vowels("aeiou"))
print(reverse_vowels("Reverse Vowels In A String"))