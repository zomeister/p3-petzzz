import ipdb

from models.adoption import Adoption
from models.pet import Pet
from models.Owner import Owner

pet1 = Pet("Fido" , 3 , "dog")
pet2 = Pet("New Jersey", 1 , "hamster")
pet3 = Pet("Taco", 44, "parrot")
pet4 = Pet("Dr. Motorcycle", 5, "cat")


own1 = Owner('Erica', "she/her")
own2 = Owner('Zoe', "she/her")

adopt1 = Adoption(own1, pet1)
adopt2 = Adoption(own1, pet4)
adopt3 = Adoption(own2, pet3)
adopt4 = Adoption(own2, pet4)


ipdb.set_trace()