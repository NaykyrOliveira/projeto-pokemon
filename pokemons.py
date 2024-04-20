tipos_pokemon = {
    'Elétrico': ['Pikachu', 'Raichu', 'Electabuzz', 'Pichu', 'Jolteon'],
    'Normal': ['Rattata', 'Persian', 'Meowth', 'Eevee', 'Snorlax', 'Lickitung'],
    'Planta': ['Chikorita', 'Cacnea', 'Sceptile', 'Turtwig', 'Leafeon', 'Meganium'],
    'Fogo': ['Charmander', 'Charmeleon', 'Arcanine', 'Flareon', 'Entei', 'Cyndaquil'],
    'Água': ['Squirtle', 'Wartortle', 'Blastoise', 'Magikarp', 'Staryu', 'Poliwag'],
    'Dragão': ['Dratini', 'Dragonair', 'Dragonite', 'Reshiram', 'Axew', 'Goodra'],
    'Psíquico': ['Abra', 'Kadabra', 'Alakazam', 'Hypno', 'Mewtwo', 'Meowstic Macho', 'Espeon', 'Mew']
}

for tipo, pokemons in tipos_pokemon.items():
    for pokemon in pokemons:
        print(f"""
class {pokemon}(Pokemon{tipo}):
    def __init__(self):
        super().__init__()
        self.nome = '{pokemon}'
        self.ataque = 'Ataque do {pokemon}'
        self.defesa = 'Defesa do {pokemon}'
    """)