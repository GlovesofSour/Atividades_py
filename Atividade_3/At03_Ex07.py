'''7. Escreva um programa que gere um dicionário, em que cada chave seja um
caractere, e seu valor seja o número desse caractere encontrado em uma
frase lida.

Exemplo:O rato -> {"O":1,"r":1,"a":1,"t":1,"o":1}'''

frase = input('Digite uma frase: ')
count = {}

for i in frase:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print(f'Frase: {frase}')
print(count)