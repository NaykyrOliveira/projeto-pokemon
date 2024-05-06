from pessoa import *
from pokemon import *


def escolher_pokemon_inicial(player):
    print('{}, Agora você poderá escolher agora o Pokemon que irá lhe acompanhar nessa jornada!'.format(player))

    pikachu = Pokemon(nome='Pikachu', level=1)
    charmander = Pokemon(nome='Charmander', level=1)
    squirtle = Pokemon(nome='Squirtle', level=1)

    print('Você possui 3 opções para escolher: ')
    print('1 - ', pikachu)
    print('2 - ', charmander)
    print('3 - ', squirtle)

    while True:
        escolha = int(input('Escolha o seu pokemon: '))
        if escolha == 1:
            player.capturar_pokemons('Pikachu')
            break
        elif escolha == 2:
            player.capturar_pokemons('Charmander')
            break
        elif escolha == 3:
            player.capturar_pokemons('Squirtle')
            break
        else:
            print('Escolha invalida')
    print(escolha)


if __name__ == '__main__':

    print('Bem - vindo ao game Pokemon RPG de terminal')
    nome = input('Olá, qual é o seu nome ? ')
    player = Player(nome)

    print('Olá {}, esse é um mundo hábitado por pokemons,'
    'e apartir de agora sua missão é se tornar um mestre dos pokemons!'.format(player))
    print('Capture o máxomo de pokemons que conseguir e lute com seus inimigos ')
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

    while True:
        print('O que você deseja fazer agora ? ')
        print('1 - Explorar pelo mapa')
        print('2 - Lutar com um inimigo')
        print('0 - Sair do jogo')

        escolha = input('Sua escolha: ')

        if escolha == '0':
            print('Fechando o jogo...')
            break
        elif escolha == '1':
            player.explorar()
        elif escolha == '2':
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
        else:
            print('Opção inválida')