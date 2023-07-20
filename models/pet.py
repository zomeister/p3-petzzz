class Pet:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age 
        self.species = species
    
    def get_name(self):
        return self._name 
    
    def set_name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 20:
            self._name = new_name
        else:
            raise Exception('Name must be a string within 20 characters!')

    name = property(get_name, set_name)

    def get_age(self):
        return self._age
    
    def set_age(self, new_age):
        if isinstance(new_age, int):
            self._age = new_age

    age = property(get_age, set_age)

    def get_species(self):
        return self._species 
    
    def set_species(self, new_species):
        if isinstance(new_species, str):
            self._species = new_species

    species = property(get_species, set_species)

    def bathe(self):
        print(f'{self.name} is taking a bubble bath!')

    def walk(self):
        print(f'{self.name} is strutting their fluff!')

    def feed(self):
        print(f'{self.name} is eating {self.species} food!')

    def sleep(self):
        print("zZzZzZzZ")


