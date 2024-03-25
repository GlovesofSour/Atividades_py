a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))

while True:
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Divisão")
    print("4 - Multiplicação")
    print("0 - Sair")
    ope = int(input("Escolha uma opção: "))

    if ope == 1:
        print(f'{a} + {b} = {a + b}')
    elif ope == 2:
        print(f'{a} - {b} = {a - b}') 
    elif ope == 3:
        print(f'{a} * {b} = {a * b}') 
    elif ope == 1:
        print(f'{a} / {b} = {a / b}')
    elif ope == 0:
        print('Finalizando programa...')
        break
    else:
        print('Resposta inválida, escolha novamente!') 