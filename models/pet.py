class Pet:
    all = []
    def __init__(self, name, age, species):
        self.name = name
        self.age = age 
        self.species = species
        self._owners = []
        self._adoptions = []
        Pet.all.append(self)
       
    def get_name(self):
        return self._name 
    def get_age(self):
        return self._age
    def get_species(self):
        return self._species 
    def set_name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 20:
            self._name = new_name
        else:
            raise Exception('Name must be a string within 20 characters!')
    def set_age(self, new_age):
        if isinstance(new_age, int):
            self._age = new_age
        else:
            raise Exception('Age must be an integer!')
    def set_species(self, new_species):
        if isinstance(new_species, str) and not hasattr(self,'_species'):
            self._species = new_species
        else:
            raise Exception('Species must be a string!')

    name = property(get_name, set_name)
    age = property(get_age, set_age)
    species = property(get_species, set_species)

    def owners(self, newb=None):
        from models.owner import Owner
        if newb and isinstance(newb, Owner) and newb not in self._owners:
            self._owners.append(newb)
        return self._owners
    def adoptions(self, newb=None):
        from models.adoption import Adoption
        if newb and isinstance(newb, Adoption):
            self._adoptions.append(newb)
        return self._adoptions
    
    def bathe(self):
        print(f'{self.name} is taking a bubble bath!')

    def walk(self):
        print(f'{self.name} is strutting their fluff!')

    def feed(self):
        print(f'{self.name} is eating {self.species} food!')

    def sleep(self):
        print("zZzZzZzZ")


