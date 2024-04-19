class Pokemon:
    def __init__(self, level=1, nome=None):
        self.level = level

        if nome:
            self.nome = nome
        else:
            self.nome = especie

    def __str__(self):
        return '{} ({})' .format(self.nome, self.level)

    def atacar(self, pokemon):
        print('{} atacou'.format(self.especie, pokemon))


class PokemonEletrico(Pokemon):pokemon.py
    tipo = 'Elétrico'

    def atacar(self, pokemon):
        print('{} lançou um Choque do Trovão em {}' .format(self.especie, pokemon))


class PokemonFogo(Pokemon):
    tipo = 'Fogo'

    def atacar(self, pokemon):
        print('{} lançou um Explosão Incineradora em {}' .format(self.especie, pokemon))


class PokemonDragao(Pokemon):
    tipo = 'Dragão'

    def atacar(self, pokemon):
        print('{} lançou um Fúria do Dragão em {}' .format(self.especie, pokemon))


class PokemonAgua(Pokemon):
    tipo = 'Água'

    def atacar(self, pokemon):
        print('{} lançou um Hidro Canhão em {}' .format(self.especie, pokemon))


class PokemonPlanta(Pokemon):
    tipo = 'Planta'

    def atacar(self, pokemon):
        print('{} lançou um  em {}' .format(self.especie, pokemon))


class Pikachu(PokemonEletrico):
    especie = 'Pikachu'


class Charmander(PokemonFogo):
    especie = 'Charmander'


class Squirtle(PokemonAgua):
    especie = 'Squirtle'


class Dragonite(PokemonDragao):
    especie = 'Charmander'


meu_pokemon = PokemonFogo('Charmander')
amigo_pokemon = PokemonEletrico('Pikachu')

print(meu_pokemon, meu_pokemon.tipo)
print(amigo_pokemon, amigo_pokemon.tipo)