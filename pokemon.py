class Pokemon:
    def __init__(self, tipo, especie, level=1, nome=None):
        self.tipo = tipo
        self.especie = especie
        self.level = level

        if nome:
            self.nome = nome
        else:
            self.nome = especie


    def __str__(self):
        return '{} ({})' .format(self.nome, self.level)


    def atacar(self, pokemon):
        print('{} atacou'.format(self.especie, pokemon))


class PokemonEletrico(Pokemon):
    def atacar(self, pokemon):
        print('{} lançou um raio do trovão em {}' .format(self.especie, pokemon))


meu_pokemon = Pokemon('Water', 'Squartle')
pokemon_amigo = PokemonEletrico('Electric', 'pikachu')

pokemon_amigo.atacar(meu_pokemon)