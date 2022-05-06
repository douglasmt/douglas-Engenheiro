'''COULDN'T do it
def extract_full_name(par_dict):
	for x in par_dict:
        for k,v in x:
'''
def extract_full_name(l):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))
    #for each value in first and last, it uses a .format with {} and {}
    # map takes the values on l(list received) AND APPLY the FUNCTION above



names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names)) # ['Elie Schoppik', 'Colt Steele']

