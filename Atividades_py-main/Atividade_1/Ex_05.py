a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('digite o valor de c: '))

d = (b ** 2) - 4 * a * c

if a == 0:
    print('O numero de "a" deve ser maior do que 0')
elif d > 0:
    print('A raiz de delta não existe')
else:
    x1 = (-b + d ** (1 / 2)) / 2 * a
    x2 = (-b - d ** (1 / 2)) / 2 * a

    print(f'O resultado de x1 é: {x1:.2f}')
    print(f'O resultado de x2 é: {x2:.2f}')
