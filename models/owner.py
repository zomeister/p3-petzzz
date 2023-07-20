
class Owner:
    def __init__(self, name, pronouns):
        self.name = name
        self.pronouns = pronouns
        

    def pets(self):
        from Adoption import Adoption
        return [a.pet for a in Adoption.all if a.owner == self ]



# class Owner:

#     def __init__ ( self, name , pronouns, adoption):
#         self.name = name
#         self.pronouns = pronouns
#         self.adoption = adoption



    # def get_name(self):
    #     return self._name
    
    # def set_name(self, new_name):
    #     if isinstance(new_name, str) and 1 <= len(new_name) <= 20:
    #         self._name = new_name
    #     else:
    #         raise Exception('Name must be a string within 20 characters!')
        
    # name = property(get_name, set_name)

    # def get_pronouns(self):
    #     return self._pronouns
    
    # def set_pronouns(self, new_pronouns):
    #     if isinstance(new_pronouns, str):
    #         self._pronouns = new_pronouns
    #     else:
    #         raise Exception('Must be a string!')
    
    # pronouns = property(get_pronouns, set_pronouns)

    # def get_adoption(self):
    #     return self._adoption
        
    # def set_adoption(self, new_adoption):
    #     if isinstance(new_adoption, Adoption):
    #         self._adoption = new_adoption
    #     else:
    #         raise Exception('Must be an instance of Adoption')
        
    # adoption = property(get_adoption, set_adoption)
    
    # def adopt(self, pet):
    #     pass
        

