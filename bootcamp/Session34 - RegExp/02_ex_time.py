import re as rege

# def is_valid_time(input):
#     time_regex = rege.compile(r'\b0?1?2?\d{1}:\d{2}\b')
#     match = time_regex.search(input)
#     if match:
#         return True # match.group()
#     return False #None

def is_valid_time(input):
    time_regex = rege.compile(r'0?1?2?\d{1}:\d{2}') #using fullmatch we take off ^ and $
    match = time_regex.fullmatch(input)
    if match:
        return True 
    return False 

print(is_valid_time("01:20"))
print(is_valid_time("1:23"))
print(is_valid_time("21:20"))
print(is_valid_time("23:20"))
print(is_valid_time("33:20"))
print(is_valid_time("3:25"))

'''udemy
def is_valid_time(input):
    pattern = re.compile(r'^\d\d?:\d\d$')
    match = pattern.search(input)
    if match:
        return True
    return False
'''