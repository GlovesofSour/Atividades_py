'''12. Crie vários dicionários, em que o nome de cada dicionário seja o nome de
um animal de estimação. Em cada dicionário, inclua o tipo do animal e o
nome do dono. Armazene esses dicionários em uma lista chamada pets.
Em seguida, percorra sua lista com um laço e, à medida que fizer isso,
apresente tudo que você sabe sobre cada animal de estimação.'''

cachorro = {'tipo': 'Cachorro', 'dono': 'João'}
gato = {'tipo': 'Gato', 'dono': 'Maria'}
passarinho = {'tipo': 'Passarinho', 'dono': 'Pedro'}
coelho = {'tipo': 'Coelho', 'dono': 'Ana'}

# Armazenando os dicionários em uma lista chamada pets
pets = [cachorro, gato, passarinho, coelho]

# Percorrendo a lista de animais de estimação com um loop
for pet in pets:
    print("\nInformações sobre o animal de estimação:")
    print("Tipo:", pet['tipo'])
    print("Dono:", pet['dono'])