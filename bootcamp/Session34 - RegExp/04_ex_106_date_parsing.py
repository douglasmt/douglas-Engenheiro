import re
def parse_date(input):
    name_regex = re.compile(r'\b(?P<day>\d{2})(\/|\,|\.)(?P<month>(1[0-2]|0?[1-9]))(\/|\,|\.)(?P<year>\d{4})\b')
    # ?P<first> to use in group below
    matches = name_regex.search(input)    
    if matches: 
        the_day = matches.group('day')
        the_month = matches.group('month')
        the_year = matches.group('year')
        date_dict = dict()
        date_dict['d'] = the_day
        date_dict['m'] = the_month
        date_dict['y'] = the_year
        return date_dict
    else:
        return None

print(parse_date("01/22/1999")) # None
print(parse_date("12,04,2003")) # { 'd': '12', 'm': 11, 'y': '2003'}
print(parse_date("12.11.2003")) # { 'd': '12', 'm': 11, 'y': '2003'}
print(parse_date("12.11.2003123")) #none

'''udemy
import re
 
def parse_date(input):
    pattern = re.compile("^(\d\d)[,/.](\d\d)[,/.](\d{4})$")
    match = pattern.search(input)
    if match:
        return {
            "d": match.group(1),
            "m": match.group(2),
            "y": match.group(3),
        }
    return None
    '''