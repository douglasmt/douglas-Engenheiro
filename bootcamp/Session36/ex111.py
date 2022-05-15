'''
sum_pairs([4,2,10,5,1], 6) # [4,2]
sum_pairs([11,20,4,2,1,5], 100) # []
'''

def sum_pairs(list_input,num_input):
    previous = 0
    for i in list_input:
        if previous:
            if (i + previous) == num_input:
                return list([previous,i])
        previous = i
    return []

print(sum_pairs([4,2,10,5,1], 6))
print(sum_pairs([11,20,4,2,1,5], 100))
print(sum_pairs([11,20,4,2,4,5], 9))

'''
def sum_pairs(ints, s):
    already_visited = set()
    for i in ints:
        difference = s - i
        if difference in already_visited:
            return [difference, i]
        already_visited.add(i)
    return []
'''
