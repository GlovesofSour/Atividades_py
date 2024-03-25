num = int(input("Digite o número da conta (até 6 dígitos): "))
soma = 0

a = int(num/100000)
b = int((num%100000)/10000)
c = int((num%10000)/1000)
d = int((num%1000)/100)
e = int(num%100/10)
f = int(num%10)

print(f"Número completo da conta: {num:0>6d}-{(a+b+c+d+e+f)%10}")
