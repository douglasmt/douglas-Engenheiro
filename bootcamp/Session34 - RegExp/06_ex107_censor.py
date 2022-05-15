import re

def censor(text):
    pattern = re.compile(r'(Frack)(([a-z])?[a-z]+)?', re.I)
    result = pattern.sub("CENSORED", text)
    return result

print(censor("Frack you"))

print(censor("I hope you fracking die"))

print(censor("your fracking frack"))

'''udemy
import re
 
def censor(input):
    pattern = re.compile(r'\bfrack\w*\b', re.IGNORECASE)
    return pattern.sub("CENSORED", input)
'''