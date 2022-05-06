class Mother:
    def __init__(self, eye_color = "brown", hair_color = "dark brown", hair_type = "curly"):
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.hair_type = hair_type

class Father:
    def __init__(self, eye_color = "blue", hair_color = "blond", hair_type = "straight"):
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.hair_type = hair_type      

class Child(Mother, Father):
    pass
'''
    def __init__(self, eye_color, hair_color, hair_type):
        super.__init__(eye_color, hair_color, hair_type)
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.hair_type = hair_type 
'''        
		