import random
import player
from other import generate_id

pets = []

prize = 100

def create_pet(name):
    global pets

    new_pet = Pet(name)
    pets.append(new_pet)

def display_information(pet):
    info = pet.get_information()

    print("Name: {}\Hunger: {}\nThirst: {}\nEnergy: {}\nHygine: {}\nID: {}".format(info["name"], info["hunger"], info["thirst"], info["energy"], info["hygine"], info["id"]))

def buy_pet():
    print("$" + str(player.money))

    if player.money >= prize:
        name = input("Please name your new pet! ")

        create_pet(name)
        player.decrease_money(prize)
    else:
        print("You don't have enough money to buy a pet!")


def get_all_pets():
    return pets

class Pet(object):
    def __init__(self, name):
        self.name = name
        self.hunger = 1
        self.thirst = 100
        self.energy = 100
        self.hygine = 100
        self.id = generate_id(amount=random.randint(20, 30))

        while True:
            self.decrease_stats(0.00001)

    def get_information(self):
        return {"name": self.name, "hunger": self.hunger, "thirst": self.thirst, "energy": self.energy, "hygine": self.hygine, "id": self.id}   

    def decrease_stats(self, amount):   
        if self.hunger >= 0:
            self.hunger -= amount

        if self.thirst >= 0:
            self.thirst -= amount

        if self.energy >= 0:
            self.energy -= amount

        if self.hygine >= 0:
            self.hygine -= amount
        
    
