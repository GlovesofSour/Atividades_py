num = int(input('Digite um valor de 5 digitos: '))

a = int(num/10000)
b = int((num%10000)/1000)
c = int((num%1000)/100)
d = int((num%100)/10)
e = int(num%10)

print(f'{a}   {b}   {c}   {d}   {e}')