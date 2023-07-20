class Adoption:
    all = []
    def __init__(self, owner, pet):

        # self.description = description
        self.owner = owner
        self.pet = pet
        Adoption.all.append(self)
        owner.adoptions(self)
        owner.pets(pet)
        pet.adoptions(self)
        pet.owners(owner)
    
    # def get_description(self):
    #     return self._description
    # def set_description(self, new_description):
    #     if type(new_description) is str and len(new_description) > 0:
    #         self._description = new_description
    #     else:
    #         raise Exception('set_description error.')
    # description = property(get_description, set_description)

    def get_owner(self):
        return self._owner 
    def get_pet(self):
        return self._pet
    def set_owner(self, new_owner):
        from models.Owner import Owner
        if isinstance(new_owner, Owner):
            self._owner = new_owner
        else:
            raise Exception('set_owner error.')
    def set_pet(self, new_pet):
        from models.Pet import Pet
        if isinstance(new_pet, Pet):
            self._pet = new_pet
        else:
            raise Exception('set_pet error.')
    owner = property(get_owner, set_owner)
    pet = property(get_pet, set_pet)

    def __repr__(self):
        return f'Adoption: {self.owner.name} adopts {self.pet.name}'