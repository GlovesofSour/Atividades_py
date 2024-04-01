'''11. Use um dicionário para armazenar informações sobre uma pessoa que
você conheça. Armazene seu primeiro nome, o sobrenome, a idade e a
cidade em que ela vive. Você deverá ter chaves como first_name,
last_name, age e city. Mostre cada informação armazenada em seu
dicionário.'''

pessoa = {
    'first_name': 'Jean',
    'last_name': 'Carvalho',
    'age': 18,
    'city': 'Luziânia'
}

print(f'Primeiro nome: {pessoa["first_name"]}')
print(f'Sobrenome: {pessoa["last_name"]}')
print(f'Idade: {pessoa["age"]}')
print(f'Cidade: {pessoa["city"]}')