list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer1 = {list1[i]:list2[i] for i in range(0,len(list1))}

print(answer1)
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
 
answer2 = dict(zip(list1,list2)) 
print(answer2)