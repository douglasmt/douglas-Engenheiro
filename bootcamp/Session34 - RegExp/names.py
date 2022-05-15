import re
def parse_name(input):
	name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')
	# ?P<first> to use in group below
	matches = name_regex.search(input)
	print(matches.group())
	print(matches.group('first'))
	print(matches.group('last'))
	print(matches.group(3))

parse_name("Mrs. Tilda Swinton")
'''
(?P<name>...)
Similar to regular parentheses, but the substring matched 
by the group is accessible via the symbolic group name name. 
Group names must be valid Python identifiers, and each group 
name must be defined only once within a regular expression. 
A symbolic group is also a numbered group, just as if the 
group were not named.
'''