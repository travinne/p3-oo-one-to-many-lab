class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")
        self.name = name
        self.pet_type = pet_type
        self.owner = None 
        Pet.all.append(self)


        if owner:
            self.set_owner(owner)
    
    def set_owner(self, owner):
        if isinstance(owner, Owner):
            self.owner = owner
        else:
            raise Exception("Owner must be an instance of Owner")
    
    pass

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Must add an instance of Pet")
        pet.set_owner(self)

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
    pass