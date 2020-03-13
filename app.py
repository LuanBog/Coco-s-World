from pet import Pet

coco = Pet("Coco")

def display_information(pet):
    info = pet.get_info()
    name = info["name"]
    health = info["health"]
    thirst = info["thirst"]
    energy = info["energy"]
    hygine = info["hygine"]
    id = info["id"]

    print("Name: {}\nHealth: {}\nThirst: {}\nEnergy: {}\nHygine: {}\nID: {}".format(name, health, thirst, energy, hygine, id))

display_information(coco)
