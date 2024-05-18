import random
from colorama import Fore

from pokemon import Pokemon


ATAQUES_POKEMON = {
    'PokemonEletrico': ['Choque do Trovão', 'Raio Solar', 'Investida Elétrica'],
    'PokemonFogo': ['Chama Fímbria', 'Lança-chamas', 'Queimadura'],
    'PokemonAgua': ['Jato de Água', 'Hidropump', 'Surf'],
    'PokemonNormal': ['Cabeçada', 'Bomba de Fumaça', 'Arranhão'],
    'PokemonPlanta': ['Vinha Chicote', 'Folha Navalha', 'Bomba de Sementes'],
    'PokemonDragao': ['Garra de Dragão', 'Cauda de Dragão', 'Fúria do Dragão'],
    'PokemonPsiquico': ['Golpe Psíquico', 'Confusão', 'Zen Headbutt'],
}


class PokemonEletrico(Pokemon):
    pokemons = ['Pikachu', 'Raichu', 'Electabuzz', 'Pichu', 'Jolteon']
    ataques = ATAQUES_POKEMON['PokemonEletrico']

    def __init__(self, nome=None, level=1):
        if nome is None:
            nome = random.choice(self.pokemons)
        super().__init__(nome=nome, especie='PokemonEletrico', level=level, ataques=self.ataques)


class PokemonNormal(Pokemon):
    pokemons = ['Rattata', 'Persian', 'Meowth', 'Eevee', 'Snorlax', 'Lickitung']
    ataques = ATAQUES_POKEMON['PokemonNormal']

    def __init__(self, nome=None, level=1):
        if nome is None:
            nome = random.choice(self.pokemons)
        super().__init__(nome=nome, especie='PokemonNormal', level=level, ataques=self.ataques)


class PokemonPlanta(Pokemon):
    pokemons = ['Chikorita', 'Cacnea', 'Sceptile', 'Turtwig', 'Leafeon', 'Meganium']
    ataques = ATAQUES_POKEMON['PokemonPlanta']

    def __init__(self, nome=None, level=1):
        if nome is None:
            nome = random.choice(self.pokemons)
        super().__init__(nome=nome, especie='PokemonPlanta', level=level, ataques=self.ataques)


class PokemonFogo(Pokemon):
    pokemons = ['Charmander', 'Charmeleon', 'Arcanine', 'Flareon', 'Entei', 'Cyndaquil']
    ataques = ATAQUES_POKEMON['PokemonFogo']

    def __init__(self, nome=None, level=1):
        if nome is None:
            nome = random.choice(self.pokemons)
        super().__init__(nome=nome, especie='PokemonFogo', level=level, ataques=self.ataques)


class PokemonAgua(Pokemon):
    pokemons = ['Squirtle', 'Wartortle', 'Blastoise', 'Magikarp', 'Staryu', 'Poliwag']
    ataques = ATAQUES_POKEMON['PokemonAgua']

    def __init__(self, nome=None, level=1):
        if nome is None:
            nome = random.choice(self.pokemons)
        super().__init__(nome=nome, especie='PokemonAgua', level=level, ataques=self.ataques)


class PokemonDragao(Pokemon):
    pokemons = ['Dratini', 'Dragonair', 'Dragonite', 'Reshiram', 'Axew', 'Goodra']
    ataques = ATAQUES_POKEMON['PokemonDragao']

    def __init__(self, nome=None, level=1):
        if nome is None:
            nome = random.choice(self.pokemons)
        super().__init__(nome=nome, especie='PokemonDragao', level=level, ataques=self.ataques)


class PokemonPsiquico(Pokemon):
    pokemons = ['Abra', 'Kadabra', 'Alakazam', 'Hypno', 'Mewtwo', 'Meowstic Macho', 'Espeon', 'Mew']
    ataques = ATAQUES_POKEMON['PokemonPsiquico']

    def __init__(self, nome=None, level=1):
        if nome is None:
            nome = random.choice(self.pokemons)
        super().__init__(nome=nome, especie='PokemonPsiquico', level=level, ataques=self.ataques)
