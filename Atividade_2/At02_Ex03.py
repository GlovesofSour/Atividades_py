num = int(input('Digite um valor para buscar por números primos: '))
n = int(input('Digite quantos números primos deseja listar: '))
count = 0
init = 2

print(f'Numeros primos encontrados no valor {num}: ')

while count < n:
    primo = True

    if init > 1:
        for i in range(2, int(init**0.5) + 1):
            if init % i == 0:
                primo = False
                break
        if primo:
            print(f'{init} ')
            count += 1
    init += 1