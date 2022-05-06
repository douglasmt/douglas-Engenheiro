'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(l1, com1, loc1, v1=0):
    if com1 == "remove":
        if loc1 == "end":
            last_item = l1[-1]
            l1.remove(last_item)
            return last_item
        elif loc1 == "beginning":
            first_item = l1[0]
            l1.remove(first_item)
            return first_item
    elif com1 == "add":
        if loc1 == "beginning":
            l1.insert(0,v1)
        elif loc1 == "end":
            l1.append(v1)
    return l1     
    

list_manipulation([1,2,3], "remove", "end") # 3 
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]       
