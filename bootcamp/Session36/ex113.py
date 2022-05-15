'''
titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"

UDEMY
Titleize

def titleize(string):
    return ' '.join(s[0].upper() + s[1:] for s in string.split(' '))

'''

name = 'Colt'
print([char.upper() for char in name])
print(name.upper())

def titleize(text_input):
    each_cap = " ".join(w[0].capitalize() + w[1:] for w in text_input.split())
    #text1 = text_input.split(' ')
    #each_cap = ''
    #for word in text1:
    #    each_cap += word.capitalize() + ' ' 
        
    return each_cap

print(titleize('this is awesome'))
print(titleize('oNLy cAPITALIZe fIRSt'))