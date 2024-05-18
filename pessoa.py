import random
from colorama import Fore

from pokemons import *
from pokemon import Ataque

NOMES = ['Jessie', 'James', 'Tyson', 'Mondo', 'Butch', 'Madame Boss', 'Archer', 'Zager', 'Sebastian', 'Pierce', 'Cassidy', 'Miyamoto', 'Attila e Hun']


class Pessoa:
    def __init__(self, nome: str = None, lvl_player: int = 0, dinheiro: int = 100, pokemons: list = None):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.lvl_player = lvl_player
        self.dinheiro = dinheiro
        self.pokemons = pokemons if pokemons else []

    def __str__(self):
        return '{} ,lvl({})'.format(self.nome, self.lvl_player)

    def mostrar_pokemons(self):
        if self.pokemons:
            print('Esses são os pokemons de {}:'.format(self))
            for index, pokemon in enumerate(self.pokemons):
                print(Fore.CYAN + '{} - {}'.format(index, pokemon))
        else:
            print('{} não possui pokemon ainda!'.format(self))

    def batalhar(self, pessoa):
        print(Fore.YELLOW + '{} iniciou a batalha com {}!'.format(self, pessoa))

        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()

        pokemon = self.escolher_pokemon()

        if pokemon and pokemon_inimigo:
            while True:
                if pokemon.ataques:
                    ataque_pokemon = random.choice(pokemon.ataques)
                    ataque_pokemon = Ataque(nome=ataque_pokemon.nome, dano=random.randint(10, 20))
                    print(Fore.GREEN + '{} atacando {} com {}!'.format(pokemon.nome, pokemon_inimigo.nome, ataque_pokemon.nome))
                else:
                    print(Fore.YELLOW + 'O Pokemon não tem ataques disponíveis')
                    return

                if pokemon.atacar(pokemon_inimigo, ataque_pokemon):
                    print(Fore.GREEN + '{} ganhou a batalha'.format(self))
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    break

                if pokemon_inimigo.ataques:
                    ataque_pokemon_inimigo = random.choice(pokemon_inimigo.ataques)
                    ataque_pokemon_inimigo = Ataque(nome=ataque_pokemon_inimigo.nome, dano=random.randint(10, 20))
                    print(Fore.RED + '{} atacando {} com {}!'.format(pokemon_inimigo.nome, pokemon.nome, ataque_pokemon_inimigo.nome))
                else:
                    print(Fore.YELLOW + 'O Pokemon inimigo não tem ataques disponíveis')
                    return

                if pokemon_inimigo.atacar(pokemon, ataque_pokemon_inimigo):
                    print(Fore.RED + '{} ganhou a batalha'.format(pessoa))
                    break

        else:
            print(Fore.YELLOW + 'Essa batalha não pode acontecer')

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print('{} escolheu {}!'.format(self, pokemon_escolhido))
            return pokemon_escolhido
        else:
            print(Fore.YELLOW + 'Erro: Esse jogador não possui nenhum pokemon para ser escolhido')


class Player(Pessoa):
    tipo = 'Player'

    def capturar_pokemons(self, pokemon):
        self.pokemons.append(pokemon)
        print('{} capturou {}'.format(self, pokemon))

    def gerar_inimigo(self):
        lvl_inimigo = random.randint(1, int(self.lvl_player * 1.5))
        return Inimigo(lvl_player=lvl_inimigo)

    def escolher_pokemon(self):
        self.mostrar_pokemons()
        if self.pokemons:
            while True:
                try:
                    escolha = int(input('Escolha o seu pokemon: '))
                    pokemon_escolhido = self.pokemons[escolha]
                    print(Fore.GREEN + '{} Eu escolho você!'.format(pokemon_escolhido))
                    return pokemon_escolhido
                except:
                    print(Fore.RED + 'Escolha inválida')
        else:
            print(Fore.YELLOW + 'Esse jogador não possui nenhum pokemon para ser escolhido')

    def mostrar_dinheiro(self):
        print('Você possui $ {}'.format(self.dinheiro))

    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print('Você ganhou $ {} dinheiro(s)!'.format(quantidade))
        self.mostrar_dinheiro()

    def explorar(self):
        if random.random() <= 0.3:
            todas_classes_pokemons = [PokemonEletrico, PokemonNormal, PokemonPlanta,
                                      PokemonFogo, PokemonAgua,
                                      PokemonDragao, PokemonPsiquico]
            classePokemon = random.choice(todas_classes_pokemons)
            pokemon = classePokemon(level=random.randint(1, 100))  # Aqui atribuímos um nível aleatório ao novo Pokémon
            print('Um pokemon selvagem apareceu: {}!'.format(pokemon))
            escolha = input('Deseja capturar o  pokemon? [s/n]: ')
            if escolha.lower() == 's':
                if random.random() >= 0.5:
                    self.capturar_pokemons(pokemon)
                else:
                    print('{} fugiu'.format(pokemon))
            elif escolha.lower() == 'n':
                print('Ok, continue explorando!')
        else:
            print('Essa exploração não deu em nada')


class Inimigo(Pessoa):
    tipo = 'Inimigo'

    def __init__(self,
                 nome: str = None,
                 lvl_player: int = random.randint(1, 1000),
                 pokemons: list = None
                 ):
        if pokemons is None:
            pokemons = []
            classes_pokemon = [PokemonEletrico, PokemonNormal, PokemonPlanta,
                               PokemonFogo, PokemonAgua,
                               PokemonDragao, PokemonPsiquico]

            for _ in range(random.randint(1, 3)):
                classe_pokemon = random.choice(classes_pokemon)
                pokemon = classe_pokemon()
                pokemons.append(pokemon)

        super().__init__(nome=nome, lvl_player=lvl_player, pokemons=pokemons)
