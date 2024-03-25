n = int(input('Digite um numero: '))
f = 1

while n < 0:
    print('O valor não pode ser negativo!')
    n = int(input('Digite novamente: '))

if n == 0:
    print(f'O fatorial de {n} é 1!')

else:
    for i in range (1, n+1):
        f *= i

    print(f"O fatorial de {n} é {f}!")