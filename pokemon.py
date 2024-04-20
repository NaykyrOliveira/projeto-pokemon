class Pokemon:
    def __init__(self,
                 level: int = 1,
                 nome: str = None,
                 ataque='Ataque básico'):

        self.level = level
        self.ataque = ataque
        self.nome = nome if nome else self.especie

    def __str__(self):
        return '{} ({})' .format(self.nome, self.level)

    def atacar(self, pokemon):
        print('{} lançou {} em {}'.format(self.especie, self.ataque, pokemon))
