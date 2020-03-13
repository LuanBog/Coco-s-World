import pet
import player

def buy_pet():
    print("$" + str(player.money))

    if player.money >= pet.prize:
        name = input("Please name your new pet! ")

        pet.create_pet(name)
        player.decrease_money(pet.prize)
    else:
        print("You don't have enough money to buy a pet!")
