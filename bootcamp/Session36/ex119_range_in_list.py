'''
range_in_list([1,2,3,4],0,2) #  6
range_in_list([1,2,3,4],0,3) # 10
range_in_list([1,2,3,4],1) #  9
range_in_list([1,2,3,4]) # 10
range_in_list([1,2,3,4],0,100) # 10
range_in_list([],0,1) # 0

UDEMY
def range_in_list(lst, start=0, end=None):
    end = end or lst[-1]
    return sum(lst[start:end+1])
'''

def range_in_list(list_in, ind_st=0, ind_end=''):
    sum_bet_ind = 0
    # print(len(list_in))
    if ind_end == '' or ind_end > len(list_in)-1:
        ind_end = len(list_in)-1
    print("{} for {} and {}".format(list_in,ind_st,ind_end) )
    
    for i in range(ind_st, ind_end+1):

        sum_bet_ind += list_in[i]
    
    return sum_bet_ind

    #return [ sum(list_in[list_item]) for list_item in range(list_in[ind_st],list_in[ind_end]) ]

print(range_in_list([1,2,3,4],0,2)) #  6
print(range_in_list([1,2,3,4],0,3)) # 10
print(range_in_list([1,2,3,4],1)) #  9
print(range_in_list([1,2,3,4])) # 10
print(range_in_list([1,2,3,4],0,100)) # 10
print(range_in_list([],0,1)) # 0