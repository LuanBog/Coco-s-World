import random

pets = []

def generate(amount=8):
    token = ""
    
    chars = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '?', '#', '$', '%')

    for i in range(amount):
        capt = random.choice([True, False])
        choice_ = random.choice(chars)
        
        if capt and choice_.isalpha():
            choice_ = choice_.upper()
            
        token = token + choice_
        
    return str(token)

def create_pet(name):
    new_pet = Pet(name)
    pets.append(new_pet)

def display_information(pet):
    info = pet.get_information()

    print("Name: {}\nHealth: {}\nThirst: {}\nEnergy: {}\nHygine: {}\nID: {}".format(info["name"], info["health"], info["thirst"], info["energy"], info["hygine"], info["id"]))

def get_all_pets():
    return pets

class Pet(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.thirst = 100
        self.energy = 100
        self.hygine = 100
        self.id = generate(amount=random.randint(20, 30))

    def get_information(self):
        return {"name": self.name, "health": self.health, "thirst": self.thirst, "energy": self.energy, "hygine": self.hygine, "id": self.id}   
