'''10. Faça um programa que ordene uma lista com o método Bubble Sort.
A ordenação pelo método de bolhas consiste em comparar dois elementos
a cada vez. Se o valor do primeiro elemento for maior que o do segundo,
eles trocarão de posição. Essa operação é então repetida para o próximo
elemento até o fim da lista. O método de bolhas exige que percorramos a
lista várias vezes. Por isso, utilizaremos um marcador para saber se
chegamos ao fim da lista trocando ou não algum elemento. Esse método
tem outra propriedade, que é posicionar maior elemento na última posição
da lista, ou seja, sua posição correta. Isso permite eliminar um elemento do
fim da lista a cada passagem completa.'''

lista = [64, 34, 25, 12, 22, 11, 90]
n = len(lista)

print(f'Lista original: {lista}')

for i in range(n):
    for j in range(0, n-i-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]

print(f'Lista ordenada: {lista}')