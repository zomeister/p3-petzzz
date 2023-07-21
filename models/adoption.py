class Adoption:
    all = []
    def __init__(self, owner, pet):
        self.owner = owner
        self.pet = pet
        Adoption.all.append(self)
        owner.adoptions(self)
        owner.pets(pet)
        pet.adoptions(self)
        pet.owners(owner)
        return
    def get_owner(self):
        return self._owner 
    def get_pet(self):
        return self._pet
    def set_owner(self, new_owner):
        from models.owner import Owner
        if isinstance(new_owner, Owner):
            self._owner = new_owner
        else:
            raise Exception('set_owner error.')
    def set_pet(self, new_pet):
        from models.pet import Pet
        if isinstance(new_pet, Pet):
            self._pet = new_pet
        else:
            raise Exception('set_pet error.')
    owner = property(get_owner, set_owner)
    pet = property(get_pet, set_pet)

    def __repr__(self):
        return f'Adoption: {self.owner.name} adopts {self.pet.name}'