'''
two_oldest_ages( [1, 2, 10, 8] ) # [8, 10]
two_oldest_ages( [6,1,9,10,4] ) # [9,10]
two_oldest_ages( [4,25,3,20,19,5] ) # [20,25]
'''

def two_oldest_ages(ages_list):
    first = 0
    second = 0 
    for i in range(0,len(ages_list)):
        for j in range(0,len(ages_list)):            
            
            if ages_list[i]> first:
                second = first
                first = ages_list[i]
            else:
                if ages_list[i]>ages_list[j]:
                    second = first
                    first = ages_list[i]
                else:
                    if ages_list[j]>first:
                        second = first
                        first = ages_list[j]
                    else:
                        if ages_list[j]>ages_list[i]:
                            second = first
                            first = ages_list[j]

            print("Comparing {} and {}. First {}, second {} ".format(ages_list[i], ages_list[j],first, second))
    return [second,first]

print(two_oldest_ages( [1, 2, 10, 8] ) )# [8, 10]
print(two_oldest_ages( [6,1,9,10,4] ) )# [9,10]
print(two_oldest_ages( [4,25,3,20,19,5] ) ) # [20,25]