import random
from colorama import Fore


class Ataque:
    def __init__(self, nome: str, dano: int):
        self.nome = nome
        self.dano = dano

    def __str__(self):
        return self.nome


class Pokemon:
    def __init__(self, level: int = None, nome: str = None, especie: str = None, pokemons: list = None, ataques: list = None):
        self.level = level if level else random.randint(1, 400)
        self.especie = especie
        self.nome = nome if nome else (random.choice(pokemons) if pokemons else especie)
        self.ataque = self.level * 5
        self.vida = self.level * 10
        self.ataques = [Ataque(nome=a, dano=random.randint(10, 20)) for a in ataques] if ataques else []

    def __str__(self):
        return f'{self.nome} {self.level}'

    def atacar(self, pokemon, ataque):
        ataque_efetivo = int((ataque.dano * random.random() * 1.3))
        pokemon.vida -= ataque_efetivo
        print(Fore.YELLOW + f'{self.nome} atacando {pokemon.nome}')
        print(Fore.RED + f'{pokemon} perdeu {ataque_efetivo} pontos de vida')
        if pokemon.vida <= 0:
            print(Fore.GREEN + f'{pokemon} foi derrotado')
            return True
        return False
