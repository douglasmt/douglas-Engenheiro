# Another class with a class attribute, used for validation purposes
class Pet:
	allowed = ['cat', 'dog', 'fish', 'rat']

	def __init__(self, name, species):
		if species not in Pet.allowed:
			raise ValueError(f"You can't have a {species} pet!")
		self.name = name
		self.species = species

	def set_species(self,species):
		if species not in Pet.allowed:
			raise ValueError(f"You can't have a {species} pet!")
		self.species = species

cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")

print("\n")
print(f"Dog name: {dog.name}")
print(f"Dog specie: {dog.species}")
print("\n")
dog.set_species("rat")

print("\n")
print(f"Cat name: {cat.name}")
print(f"Cat specie: {cat.species}")
print("\n")

print("\n")
print(f"Dog name: {dog.name}")
print(f"Dog specie after change: {dog.species}")
print("\n")

# 
Pet.allowed.append("lion")
Pet.allowed.append("pig")
lion = Pet("Lion King", "lion")

print("\n")
print(f"Lion name: {lion.name}")
print(f"Lion specie after change: {lion.species}")
print("id Lion Object: " + str(id(lion.allowed)))
print("\n")
print("id Pet Class: " + str(id(Pet.allowed)))









