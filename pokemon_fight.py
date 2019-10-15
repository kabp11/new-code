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