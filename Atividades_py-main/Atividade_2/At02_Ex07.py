num = input("Digite o número da conta (até 6 dígitos): ")
soma = 0

for i in num:
    soma += int(num)

d = soma % 10

tam =  6 - len(num)

conta = "0" * tam + num + "-" + str(d)

print("Número completo da conta:", conta)