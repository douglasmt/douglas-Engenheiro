# make sure your solution is assigned to the answer variable so the tests can work!
answer = {}.fromkeys({'a','e','i','o','u'},0) #my answer

answer = {char:0 for char in 'aeiou'}
answer = dict.fromkeys("aeiou", 0) 