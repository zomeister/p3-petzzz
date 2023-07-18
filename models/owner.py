from pet import Pet
# from task import Task

class Owner () :

    def __init__(self, name='John Doe'):
        self.name = name
        self.pets = []
    
    def add_pet(self, name, age, species):
        self.pets.append(Pet(name, age, species))
        pass
        
    pass