import random

from pokemon import Pokemon


class PokemonEletrico(Pokemon):
    pokemons = ['Pikachu', 'Raichu', 'Electabuzz', 'Pichu', 'Jolteon']

    def __init__(self, nome=None):
        if nome:
            super().__init__(nome)
        else:
            super().__init__(random.choice(self.pokemons))


class PokemonNormal(Pokemon):
    pokemons = ['Rattata', 'Persian', 'Meowth', 'Eevee', 'Snorlax', 'Lickitung']

    def __init__(self, nome=None):
        if nome:
            super().__init__(nome)
        else:
            super().__init__(random.choice(self.pokemons))


class PokemonPlanta(Pokemon):
    pokemons = ['Chikorita', 'Cacnea', 'Sceptile', 'Turtwig', 'Leafeon', 'Meganium']

    def __init__(self, nome=None):
        if nome:
            super().__init__(nome)
        else:
            super().__init__(random.choice(self.pokemons))


class PokemonFogo(Pokemon):
    pokemons = ['Charmander', 'Charmeleon', 'Arcanine', 'Flareon', 'Entei', 'Cyndaquil']

    def __init__(self, nome=None):
        if nome:
            super().__init__(nome)
        else:
            super().__init__(random.choice(self.pokemons))


class PokemonAgua(Pokemon):
    pokemons = ['Squirtle', 'Wartortle', 'Blastoise', 'Magikarp', 'Staryu', 'Poliwag']

    def __init__(self, nome=None):
        if nome:
            super().__init__(nome)
        else:
            super().__init__(random.choice(self.pokemons))


class PokemonDragao(Pokemon):
    pokemons = ['Dratini', 'Dragonair', 'Dragonite', 'Reshiram', 'Axew', 'Goodra']

    def __init__(self, nome=None):
        if nome:
            super().__init__(nome)
        else:
            super().__init__(random.choice(self.pokemons))


class PokemonPsiquico(Pokemon):
    pokemons = ['Abra', 'Kadabra', 'Alakazam', 'Hypno', 'Mewtwo', 'Meowstic Macho', 'Espeon', 'Mew']

    def __init__(self, nome=None):
        if nome:
            super().__init__(nome)
        else:
            super().__init__(random.choice(self.pokemons))
