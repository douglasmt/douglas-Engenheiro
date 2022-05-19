setc = {'NY', 'Seattle'}
print(setc)
set1 = {'NY', 'Seattle'}
print(set1)
set1.add("Limeira")
setc.add("Socorro") 

print(setc)
print(set1)

print("Everything outer join : " + str(set1 | setc)) 
print("Intersection inner join : " + str(set1 & setc) )
