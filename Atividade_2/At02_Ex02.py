num = int(input('Digite um valor: '))
count = 0

for i in range(1,num+1):

    if num % i == 0:
        count += 1

if count == 2:
    print(f'o numero {num} é primo!')
else:
    print('não é primo')
