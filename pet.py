import random

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

class Pet(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.thirst = 100
        self.energy = 100
        self.hygine = 100
        self.ID = generate(amount=random.randint(20, 30))

    def get_info(self):
        return {"name": self.name, "health": self.health, "thirst": self.thirst, "energy": self.energy, "hygine": self.hygine, "id": self.ID}
        