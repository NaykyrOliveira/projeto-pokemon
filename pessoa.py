from pokemons import *


class Pessoa:
    def __init__(self,
                 nome: str = None,
                 pokemons: list = []):

        if nome:
            self.nome = nome
        else:
            self.nome = 'Anônimo'

        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        for pokemon in self.pokemons:
            print(pokemon)


class Player(Pessoa):
    tipo = 'Player'


class Inimigo(Pessoa):
    tipo = 'Inimigo'