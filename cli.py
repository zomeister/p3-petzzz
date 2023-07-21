from rich.console import Console

console = Console(width=80)

def rich_print(text, style="#FFFFFF", justify="left"):
    console.print(text, style=style, justify=justify)
def title(text):
    style = "underline white on blue"
    rich_print(text, style=style, justify="center")
def option(text):
    style = "bold #af00ff"
    rich_print(text, style=style, justify="left")
def loading(text):
    pass

class CLI():
    def __init__(self):
        self.start()
        
    def start(self):
        exit = False
        from models.owner import Owner
        while not exit:
            self.print_menu()
            
            selection = input("Select option to continue...  ")
            if selection == '1':
                console.print("Adopting a pet...")
                
                title('Welcome to the adoption center!')
                owner_name = input('Enter name: ')
                owner_pronouns = input('Enter pronouns: ')
                owner = Owner(owner_name, owner_pronouns)
                if owner:
                    print(f'Welcome {owner.name}!')
                else:
                    raise Exception('Owner not created.')
            elif selection == "2":
                print('Directing to pet care menu...')
                pet = self.print_pets()
                self.print_pet_menu(pet)
            elif selection == 'q':
                print("Exiting...")
                self.end()
                exit = True
            else:
                print("Invalid selection. Please try again.")
    def end(self):
        print("{:^20}".format('Goodbye!'))
        
    def print_menu(self):
        title("Welcome to PetZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZzZ")
        option("1 - Adopt a pet")
        option("2 - Care for pet")
        option("q - Quit")
    def print_pet_menu(self, pet):
        title('Pet Menu')
        option('1 - Feed')
        option('2 - Walk')
        option('3 - Bathe')
        option('4 - Sleep')
        option('q - Quit')
        selection = input('Select option to continue...  ')
        if selection == '1':
            pet.feed()
        elif selection == '2':
            pet.walk()
        elif selection == '3':
            pet.bathe()
        elif selection == '4':
            pet.sleep()
    def print_pets(self):
        from models.pet import Pet
        Pet("Fido" , 3 , "dog")
        Pet("New Jersey", 1 , "hamster")
        Pet("Taco", 44, "parrot")
        Pet("Dr. Motorcycle", 5, "cat")
        for pet in Pet.all:
            print(pet.name)
        selection = input('Select pet to adopt...  ')
        for pet in Pet.all:
            if pet.name.lower() == selection.lower():
                print(f'You adopted a {pet.species} called {pet.name}!')
                return pet
        

CLI()
