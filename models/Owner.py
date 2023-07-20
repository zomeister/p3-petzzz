class Owner:
    def __init__ ( self, name , pronouns):
        self.name = name
        self.pronouns = pronouns
        self._pets = []
        self._adoptions = []
    
    def get_name(self):
        return self._name
    def get_pronouns(self):
        return self._pronouns
    def set_name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 20:
            self._name = new_name
        else:
            raise Exception('Name must be a string within 20 characters!')
    def set_pronouns(self, new_pronouns):
        if isinstance(new_pronouns, str):
            self._pronouns = new_pronouns
        else:
            raise Exception('Must be a string!')
    name = property(get_name, set_name)
    pronouns = property(get_pronouns, set_pronouns)

    def pets(self, newb=None):
        from models.Pet import Pet
        if newb and isinstance(newb, Pet):
            self._pets.append(newb)
        return self._pets
    def adoptions(self, newb=None):
        from models.Adoption import Adoption
        if newb and isinstance(newb, Adoption):
            self._adoptions.append(newb)
        return self._adoptions
    
    def adopt(self, pet):
        pass
        

