num = int(input('Digite um valor: '))
n = int(input('Quantos numeros primos deseja apresentar?'))
count = 0

for i in range(1,num+1):

    if num % i == 0:
        count += 1
        if count == 2 and count < n:
            print(f'primo: {i}')

