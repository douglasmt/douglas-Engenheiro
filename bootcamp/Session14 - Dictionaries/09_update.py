instructor = {"name" : "Douglas", "age" : 36, "job": "data"}
person = {"city": "São Paulo"}
person.update(instructor)
print("\n person : " + str(person)) # is a new object updated with instructor data
print("\n instructor : " + str(instructor))

person['name'] = "Fabio"
print("\n person with name updated: " + str(person)) # is a new object updated with instructor data
print("\n instructor : " + str(instructor))

person.update(instructor)
print("\n person : " + str(person)) # is a new object updated with instructor data
print("\n instructor : " + str(instructor))

person.update({})

person.update(instructor)
print("\n person after person.update(\{}): " + str(person)) # is a new object updated with instructor data
print("\n instructor : " + str(instructor))
