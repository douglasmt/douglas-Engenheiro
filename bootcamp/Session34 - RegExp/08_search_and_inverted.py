import re
titles = [
    "Significant Others (1987)",
    "Tales of the City (1978)",
    "The Days of Anna Madrigal (2014)",
    "Mary Ann in Autumn (2010)",
    "Further Tales of the City (1982)",
    "Babycakes (1984)",
    "More Tales of the City (1980)",
    "Sure of You (1989)",
    "Michael Tolliver Lives (2007)"
]
titles.sort()
print(titles)

pattern = re.compile(r'(^[\w ]+) (\(\d{4}\))')
result = pattern.sub("\g<2> - \g<1>", titles[0])
# \g<2>  is the year: \(\d{4}\) 
# \g<1> is the title: ^[\w ]+
# it will reverse the text
print(result)

pattern = re.compile(r'(^[\w ]+) \((\d{4})\)')
result = pattern.sub("\g<2> - \g<1>", titles[0])
# \((\d{4})\) will remove the parentheses
print(result)