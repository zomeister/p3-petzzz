main_menu = '''MAIN MENU
(3) op 3 - adopt a pet
(4) op 4 - care for pet
(q) exit
'''
class CLI():
    def __init__(self):
        self.start()
        
    def start(self):
        exit = False
        while not exit:
            print(main_menu)
            selection = input("Select option to continue...  ")
            # if selection == 1:
            #     print("Registering as owner...")
            # elif selection == 2:
            #     print("Registering a pet...")
            if selection == 3:
                print("Adopting a pet...")
            elif selection == 4:
                print('Directing to pet care menu...')
            elif selection == 'q':
                print("Exiting...")
                self.end()
                exit = True
            else:
                print("Invalid selection. Please try again.")
    def end(self):
        print("{:^20}".format('Goodbye!'))

CLI()
