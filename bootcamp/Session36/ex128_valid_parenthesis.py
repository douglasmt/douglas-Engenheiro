'''
valid_parentheses("()") # True 
valid_parentheses(")(()))") # False 
valid_parentheses("(") # False 
valid_parentheses("(())((()())())") # True 
valid_parentheses('))((') # False
valid_parentheses('())(') # False
valid_parentheses('()()()()())()(') # False
'''

def valid_parentheses(par):
    count_par1 = 0
    for i in range(0,len(par)-1):
        count_par1 += 1
        print("vendo o i")
        print(par[i])
        if par[i] == '(':
            for j in range(i+1,len(par)):
                print("vendo o j")
                print(par[j])
                if par[j] == ')':
                    count_par1 += 1
    print(count_par1)
    if count_par1 % 2 == 0 and count_par1 != 0:
        return True
    return False
    
# print(valid_parentheses("()"))
# print(valid_parentheses(")(()))"))
print(valid_parentheses("("))
print(valid_parentheses("(())((()())())"))
# print(valid_parentheses('))(('))