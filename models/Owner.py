
class Owner:

    def __init__ ( self, name , pronouns, adoption):
        self.name = name
        self.pronouns = pronouns

    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 20:
            self._name = new_name
        else:
            raise Exception('Name must be a string within 20 characters!')
        
    name = property(get_name, set_name)

    def get_pronouns(self):
        return self._pronouns
    
    def set_pronouns(self, new_pronouns):
        if isinstance(new_pronouns, str):
            self._pronouns = new_pronouns
        else:
            raise Exception('Must be a string!')
    
    pronouns = property(get_pronouns, set_pronouns)

    def adopt(self, pet):
        pass
        








