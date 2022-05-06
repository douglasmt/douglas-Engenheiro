'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''

def compact(l1):
    return list([l for l in l1 if l])

print(compact([0,1,2,"",[], False, {}, None, "All done"])) # [1,2, "All done"])


'''Without a list comprehension
I make a list to store all truthy values
I iterate over each value in the list
I check if the value is truthy (using a simple if val )
If the value is truthy, add it to the truthy_vals  list
return truthy_vals  at the end
'''
def compact(l):
    truthy_vals = []
    for val in l:
        if val: truthy_vals.append(val)
    return truthy_vals
   