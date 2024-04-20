import random


class Pokemon:
    def __init__(self,
                 level: int = None,
                 nome: str = None,
                 especie: str = None,
                 pokemons: list = None
                 ):
        if level:
            self.level = level
        else:
            self.level = random.randint(1, 400)

        self.especie = especie

        if nome:
            self.nome = nome
        elif pokemons:
            self.nome = random.choice(pokemons)
        else:
            self.nome = self.especie

    def __str__(self):
        return '{} ({})' .format(self.nome, self.level)

    def atacar(self, pokemon):
        print('{} lançou um ataque em {}'.format(self.nome, pokemon))