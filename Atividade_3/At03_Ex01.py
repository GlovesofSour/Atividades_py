'''1. Vamos tentar resolver alguns desafios. Dada a lista = [12, -2, 4, 8, 29, 45,
78, 36, -17, 2, 12, 8, 3, 3,-52] faça um programa que:
a. imprima o maior elemento;
b. imprima o menor elemento;
c. imprima os números pares;
d. imprima o número de ocorrências do primeiro elemento da lista;
e. imprima a média dos elementos;
f. imprima a soma dos elementos de valor negativo'''

lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
pares = []
maior = 0
menor = 0
ocorrencia = 0
soma = 0
soma_neg = 0
x = 0

for i in lista:
    
    if i > maior:
        maior = i
    
    if i < maior:
        menor = i

    if i % 2 == 0:
        pares.append(i)

    if i == lista[0]:
        ocorrencia += 1

    if i < 0:
        soma_neg += i

    soma += i
    x += 1

print(f'a) Maior número: {maior}')
print(f'b) Menor número: {menor}')
print(f'c) Numeros pares: {pares}')
print(f'd) Número de ocorrências do primeiro número: {ocorrencia}')
print(f'e) Média dos números: {soma/x:.2f}')
print(f'e) soma dos números negativos: {soma_neg}')
