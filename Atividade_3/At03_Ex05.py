'''5. Escreva um programa que copie os valores pares para uma lista e os
valores ímpares para outra lista. A lista inicialmente de valores é V=
[9,8,7,12,0,13,21] .'''

V = [9, 8, 7, 12, 0, 13, 21]
impares = []
pares = []

for i in V:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(f'Lista de impares: {impares}')
print(f'Lista de pares: {pares}')