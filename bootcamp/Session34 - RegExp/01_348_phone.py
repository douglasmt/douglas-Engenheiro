import re as rege

def extract_phone(input):
    phone_regex = rege.compile(r'\b\d{2} \d{5}-\d{4}\b')
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None

def extract_all_phones(input):
    phone_regex = rege.compile(r'\b\d{2} \d{5}-\d{4}\b')
    return phone_regex.findall(input)

print(extract_phone("My number is 11 98176-6213"))
print(extract_phone("My number is 11 26795833 or call me at 11 98176-6213"))

# print(extract_all_phones("My number is 11 32679-5833 or call me at 11 98176-6213"))

# def is_valid_phone(input):
#     phone_regex = rege.compile(r'^\d{2} \d{5}-\d{4}$') #now it has a start and an end
#     match = phone_regex.search(input) # using search 
#     if match:
#         return True
#     return False

def is_valid_phone(input):
    phone_regex = rege.compile(r'\d{2} \d{5}-\d{4}') #using fullmatch we take off ^ and $
    match = phone_regex.fullmatch(input) # using fullmatch 
    if match:
        return True
    return False    
'''
print(is_valid_phone("11 98176-6213"))
print(is_valid_phone("11 26795833"))
print(is_valid_phone("asd11 26795-8331sd"))
'''
