import random


NOMES = [
        'Jessie', 'James', 'Tyson', 'Mondo', 'Butch',
        'Madame Boss', 'Archer', 'Zager', 'Sebastian',
        'Pierce', 'Cassidy', 'Miyamoto', 'Attila e Hun'
    ]


class Pessoa:

    def __init__(self,
                 nome: str = None,
                 lvl_player: int = 0,
                 pokemons: list = []):

        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.lvl_player = lvl_player
        self.pokemons = pokemons

    def __str__(self):
        return '{} ,lvl({})'.format(self.nome, self.lvl_player)

    def mostrar_pokemons(self):
        if self.pokemons:
            print('Esses são os pokemons de {}:'.format(self))
            for pokemon in self.pokemons:
                print(pokemon)
        else:
            print('{} não possui pokemon ainda!'.format(self))


class Player(Pessoa):
    tipo = 'Player'

    def capturar_pokemons(self, pokemon):
        self.pokemons.append(pokemon)
        print('{} capturou {}'.format(self, pokemon))

    def gerar_inimigo(self):
        lvl_inimigo = random.randint(1, int(self.lvl_player * 1.5))

        return Inimigo(lvl_player=lvl_inimigo)


class Inimigo(Pessoa):
    tipo = 'Inimigo'

    def __init__(self,
                 nome: str = None,
                 lvl_player: int = random.randint(1, 1000),
                 pokemons: list = []
                 ):
        if not pokemons:
            for i in range(random.randint(1, 3)):
                pokemons.append(random.choice())

        super().__init__(nome=nome, lvl_player=lvl_player, pokemons=pokemons)