# DON'T TOUCH THIS PLEASE!
people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
# DON'T TOUCH THIS PLEASE!
i = 0
#Change "Hanna" to "Hannah"
while i < len(people):
    if people[i] == "Hanna":
        people[i] = "Hannah"
    if people[i] == "Geoffrey":
        people[i] = "Jeffrey"
    if people[i] == "aparna":
        people[i] = people[i].capitalize()
    i += 1
    

print(people)
