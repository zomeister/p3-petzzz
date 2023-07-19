from models.Owner import Owner
from models.Pet import Pet

class Adoption:
    all = []
    def __init__(self, description, owner, pet):
        self.description = description
        self.owner = owner
        self.pet = pet
        Adoption.all.append(self)

    def get_description(self):
        return self._description

    def set_description(self, new_description):
        if type(new_description) is str:
            self._description = new_description
        else:
            raise Exception('Description must be a string!')

    def get_owner(self):
        return self._owner 
    
    def set_owner(self, new_owner):
        if isinstance(new_owner, Owner):
            self._owner = new_owner

    owner = property(get_owner, set_owner)

    def get_pet(self):
        return self._pet
    
    def set_pet(self, new_pet):
        if isinstance(new_pet, Pet):
            self._pet = new_pet

    pet = property(get_pet, set_pet)