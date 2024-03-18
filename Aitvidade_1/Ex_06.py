N = int(input('Digite um numero: '))

h = N//3600
r = N%3600
m = r//60
s = r%60

print(f"{h}:{m}:{s}")