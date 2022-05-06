'''
self._age is private attribute
JUST EXAMPLES to try to understand

def
'''
class Human:
    def __init__(self,name, age):
        self.name = name
        if age >=0:
            self._age = age

    @property
    def get_age(self):
        return self._age
    
    @age.setter
    def age(self,value):
        if value >=0:
            self._age = value