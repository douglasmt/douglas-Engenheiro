class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level

class NPC(Character):
	def __init__(self, name, hp, level):
		super().__init__(name, hp, level) # Call init on parent class
    
	def speak(self):
		print("This is the speech")

villager = NPC("Bob", 100, 12)        
print(villager.name)
print(villager.hp)
print(villager.level)
villager.speak()