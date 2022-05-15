import re
def parse_date(input):
	name_regex = re.compile(r'\b(?P<day>\d{2})(\/|\,|\.)(?P<month>\d{2})(\/|\,|\.)(?P<year>\d{4})\b')
	# ?P<first> to use in group below
	matches = name_regex.search(input)
    
    the_day = matches.group('day')
    the_month = matches.group('month')
    the_year = matches.group('year')