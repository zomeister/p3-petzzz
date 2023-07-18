class Pet:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age 
        self.species = species
    
    def bathe(self):
        print(f'{self.name} is taking a bubble bath!')

    def walk(self):
        print(f'{self.name} is strutting their fluff!')

    def feed(self):
        print(f'{self.name} is eating {self.species} food!')

    def sleep(self):
        print("zZzZzZzZ")


