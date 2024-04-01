'''4. A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T= [
-10, -8, 0, 1, 2, 5, -2,-4]. Faça um programa que imprima a menor e a maior
temperatura, assim como a temperatura média.'''

T= [-10, -8, 0, 1, 2, 5, -2,-4]

maior = 0
menor = 10
soma = 0
x = 0

for i in T:
    
    if i > maior:
        maior = i
    
    if menor > i:
        menor = i

    soma += i
    x += 1

print(f'Maior Temperatura: {maior}')
print(f'Menor Temperatura: {menor}')
print(f'Temperatura média: {soma/x:2}')