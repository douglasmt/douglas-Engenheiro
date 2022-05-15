import re
text = "Last night Mrs. Daisy and Mr. white murdered Ms. Chow"

pattern = re.compile(r'(Mr.|Mrs.|Ms.) ([a-z])[a-z]+', re.I)
# pattern is a re function to be used in result variable
# takes (Mr.|Mrs.|Ms.) and the first Letter after it
# re.I ignores upper and lower cases

result = pattern.sub("\g<1> \g<2>", text)
# result variable is the execution of pattern on the text value
# in a string passed to the repl argument of re.sub()
# \g<quote> 
# \g<1>
# \1

print(result)

