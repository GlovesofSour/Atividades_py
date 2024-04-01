'''8. Escreva um programa que compare duas listas. Utilizando operações com
conjuntos, imprima:
os valores comuns às duas listas
os valores que só existem na primeira
os valores que existem apenas na segunda
uma lista com os elementos não repetidos das duas listas.
a primeira lista sem os elementos repetidos na segunda'''

lista1 = [2, 4, 6, 8, 10, 12]
lista2 = [2, 6, 10, 14, 18, 22]

a = set(lista1)
b = set(lista2)

print(f'Valores comuns nas duas listas: {a & b}')
print(f'Valores que só existem na primeira lista: {a - b}')
print(f'Valores que existem apenas na segunda lista: {b - a}')
print(f'Lista com elementos não repetidos das duas listas: {list(b | a)}')
print(f'A primeira lista sem os elementos repetidos na segunda: {list(a - b)}')