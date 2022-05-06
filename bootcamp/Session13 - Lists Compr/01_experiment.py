friends = ["ashley","matt","michael"]
print(friends[0])
#'ashley'
print(friends[0].upper())
#'ASHLEY'
print(friends[0].upper())
#'ASHLEY'
print(friends[0].upper())
#'ASHLEY'

print([friend[0].upper() + friend[1:] for friend in friends] )
print([friend[0].upper() + friend[1:] for friend in friends])
#['Ashley', 'Matt', 'Michael']

print( "upper on the last letter(Y) + from the last letter to the end (y) ['Yy', 'Tt', 'Ll']")
print([friend[-1].upper() + friend[-1:] for friend in friends])

print("upper on the 3rd letter (H) + the last letter(y) ['Hy', 'Tt', 'Cl']") 
print( [friend[2].upper() + friend[-1:] for friend in friends])

print("upper on the 2nd letter and +entire word ['Hashley', 'Tmatt', 'Cmichael']")
print([friend[2].upper() + friend[:] for friend in friends])

print("upper on the 2nd letter and + entire word without the last letter ['Hashle', 'Tmat', 'Cmichae']")
print([friend[2].upper() + friend[:-1] for friend in friends])


print("upper on 2nd letter + name inverted: ['Hyelhsa', 'Tttam', 'Cleahcim']") 
print([friend[2].upper() + friend[::-1] for friend in friends])

print("upper on last letter + inverted name: ['Yyelhsa', 'Tttam', 'Lleahcim']") 
print([friend[-1].upper() + friend[::-1] for friend in friends])

print("upper last letter + no word because it is until the last character ['Y', 'T', 'L']")
print([friend[-1].upper() + friend[:-1:-1] for friend in friends])

print("upper last letter + from last letter inverted word: ['Yyelhsa', 'Tttam', 'Lleahcim']")
print([friend[-1].upper() + friend[-1::-1] for friend in friends])

print("upper last letter + word inverted from the first to penultimate character ['Yelhsa', 'Ttam', 'Leahcim']")
print( [friend[-1].upper() + friend[-2::-1] for friend in friends])
