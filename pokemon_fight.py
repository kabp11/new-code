<<<<<<< HEAD
pokemon_choised = input("with which pokemon Do You want to fight {squirtle / charmander / bulbasur}: ")

life_of_pikachu = 100
life_of_rival = 0
atack_pokemon = 0

if pokemon_choised == "squirtle":
    life_of_rival = 90
    name_pokemon = "squirtle"
    atack_pokemon = 12
elif pokemon_choised == "charmander":
    life_of_rival = 100
    name_pokemon = "charmander"
    atack_pokemon = 15
elif pokemon_choised == "bulbasur":
    life_of_rival = 80
    name_pokemon = "bulbasur"
    atack_pokemon = 10

while life_of_pikachu > 0 and life_of_rival > 0:
    atack_choised = input("which atack Do You want to use {punch / thunderball")
    #choise the atack
    if atack_choised == "punch":
        life_of_rival -=10
        print("not effective")
    if atack_choised == "thunderball":
        life_of_rival -= 20
        print("effective")

    print("the life of {} is {}".format(name_pokemon, life_of_rival))
    #the enemigue atack
    print("{} atacked you".format(name_pokemon))
    life_of_pikachu -= atack_pokemon

    print("your life now is {}".format(life_of_pikachu))

if life_of_rival <= 0:
    print("you win")

if life_of_pikachu <= 0:
    print("you lose")

print("the fight is over")
=======
pokemon_choised = input("with which pokemon Do You want to fight {squirtle / charmander / bulbasur}: ")

life_of_pikachu = 100
life_of_rival = 0

if pokemon_choised == "squirtle":
    life_of_rival = 90

if pokemon_choised == "charmander":
    life_of_rival = 100

if pokemon_choised == "bulbasur":
    life_of_rival = 80

while life_of_pikachu > 0 and life_of_rival > 0:
    atack_choised = input("which atack Do You want to use {punch / thunderball")
    if atack_choised == "punch":
        life_of_rival -=10
    if atack_choised == "thunderball":
        life_of_rival -= 20

print("el combate ha terminado")
=======
pokemon_choised = input("with which pokemon Do You want to fight {squirtle / charmander / bulbasur}: ")

life_of_pikachu = 100
life_of_rival = 0
atack_pokemon = 0

if pokemon_choised == "squirtle":
    life_of_rival = 90
    name_pokemon = "squirtle"
    atack_pokemon = 12
elif pokemon_choised == "charmander":
    life_of_rival = 100
    name_pokemon = "charmander"
    atack_pokemon = 15
elif pokemon_choised == "bulbasur":
    life_of_rival = 80
    name_pokemon = "bulbasur"
    atack_pokemon = 10

while life_of_pikachu > 0 and life_of_rival > 0:
    atack_choised = input("which atack Do You want to use {punch / thunderball")
    #choise the atack
    if atack_choised == "punch":
        life_of_rival -=10
        print("not effective")
    elif atack_choised == "thunderball":
        life_of_rival -= 20
        print("effective")

    print("the life of {} is {}".format(name_pokemon, life_of_rival))
    #the enemigue atack
    print("{} atacked you".format(name_pokemon))
    life_of_pikachu -= atack_pokemon

    print("your life now is {}".format(life_of_pikachu))

if life_of_rival <= 0:
    print("you win")

elif life_of_pikachu <= 0:
    print("you lose")

print("the fight is over")
>>>>>>> poniendo el archivo test
