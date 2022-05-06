import keyword
def contains_keyword(*argument):
    #args_k = list(argument)
    for k in argument:# args_k:
        #print(k)
        if keyword.iskeyword(k):            
            checking = True
            break
        else:
            checking = False
        
    return checking

print(contains_keyword("hello", "goodbye","def"))
print(contains_keyword("hello", "goodbye","crisis"))