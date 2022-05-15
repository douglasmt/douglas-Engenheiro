'''
min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'}) # [1,10]
min_max_key_in_dictionary({1: "Elie", 4:"Matt", 2: "Tim"}) # [1,4]
'''

def min_max_key_in_dictionary(dic_in):
    dic_low_high = []
    for k,v in dic_in.items():
        print(f"Key is {k} and value is {v}")
        dic_low_high.append(k)
    dict_res = []
    dict_res.append(min(dic_low_high))
    dict_res.append(max(dic_low_high))

    return dict_res

print(min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'})) # [1,10]
print(min_max_key_in_dictionary({1: "Elie", 4:"Matt", 2: "Tim"})) # [1,4]
