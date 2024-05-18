import colorama
import random
import pickle

from colorama import Fore, Style
from pessoa import Player, Inimigo
from pokemons import PokemonEletrico, PokemonFogo, PokemonAgua, PokemonPlanta

colorama.init(autoreset=True)


def escolher_pokemon_inicial(player):
    print(Fore.YELLOW + '{}, agora você poderá escolher o Pokemon que irá lhe acompanhar nessa jornada!'.format(player))

    pikachu = PokemonEletrico(nome='Pikachu', level=1)
    charmander = PokemonFogo(nome='Charmander', level=1)
    squirtle = PokemonAgua(nome='Squirtle', level=1)

    print('Você possui 3 opções para escolher:')
    print('1 - ', pikachu)
    print('2 - ', charmander)
    print('3 - ', squirtle)

    while True:
        escolha = input('Escolha o seu pokemon: ')
        if escolha == '1':
            player.capturar_pokemons(pikachu)
            break
        elif escolha == '2':
            player.capturar_pokemons(charmander)
            break
        elif escolha == '3':
            player.capturar_pokemons(squirtle)
            break
        else:
            print(Fore.RED + 'Escolha inválida')


def salvar_jogo(player):
    try:
        with open('database.db', 'wb') as arquivo:
            pickle.dump(player, arquivo)
            print('Jogo Salvo com sucesso!')
    except Exception as erro:
        print('Erro ao salvar o jogo')
        print(erro)


def carregar_jogo():
    try:
        with open('database.db', 'rb') as arquivo:
            player = pickle.load(arquivo)
            print('Loading feito com sucesso!')
            return player
    except Exception as erro:
        print('Save não encontrado, vamos iniciar um novo jogo?')


if __name__ == '__main__':
    print(Fore.GREEN + 'Bem-vindo ao game Pokemon RPG de terminal')

    player = carregar_jogo()

    if not player:
        nome = input('Qual é o seu nome? ')
        player = Player(nome)

        print('Olá {}, esse é um mundo habitado por pokemons, e a partir de agora sua missão é se tornar um mestre dos pokemons!'.format(player))
        print('Capture o máximo de pokemons que conseguir e lute com seus inimigos.')
        player.mostrar_dinheiro()

        if player.pokemons:
            print('Já vi que você possui alguns pokemons')
            player.mostrar_pokemons()
        else:
            print('Você não possui nenhum pokemon, portanto precisa escolher um para iniciar a sua jornada')
            escolher_pokemon_inicial(player)

        print('Agora que você capturou o seu primeiro pokemon, enfrente o seu primeiro inimigo')

        primeiro_inimigo = Inimigo()
        player.batalhar(primeiro_inimigo)
        salvar_jogo(player)

    while True:
        print('O que você deseja fazer agora? ')
        print('1 - Explorar pelo mapa')
        print('2 - Lutar com um inimigo')
        print('3 - Mostrar Pokédex')
        print('0 - Sair do jogo')

        escolha = input('Sua escolha: ')

        if escolha == '0':
            print('Fechando o jogo...')
            break
        elif escolha == '1':
            player.explorar()
            salvar_jogo(player)
        elif escolha == '2':
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo(player)
        elif escolha == '3':
            player.mostrar_pokemons()
        else:
            print(Fore.RED + 'Opção inválida')
