from pessoa import *


meu_pokemon = Pikachu()
meu_pokemon2 = Charmander()

eu = Player(nome='Ash', pokemons=[meu_pokemon, meu_pokemon2])

print(eu)
eu.mostrar_pokemons()

