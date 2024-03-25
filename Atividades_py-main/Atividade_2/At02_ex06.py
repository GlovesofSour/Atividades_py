n = int(input('Digite um numero maior do que 2: '))

while n < 3:
    print('O valor deve ser 3 ou maior')
    n = int(input('Digite novamente: '))

a, b = 1, 1

for i in range (3,n+1):
   a, b = b, a + b

print(f'O numero {n} da seuquencia de fibonacci será {b}')