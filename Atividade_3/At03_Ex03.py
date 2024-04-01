'''3. Faça um programa que leia uma expressão com parênteses. Usando
pilhas, verifique se os parênteses foram abertos e fechados na ordem
correta.
Exemplo:
(()) OK
()()(()()) OK
( ) ) Erro
Listas, Dicionários, Tuplas e Conjuntos 23
Você pode adicionar elementos à pilha sempre que encontrar abre
parênteses e desempilhá-la a cada fecha parênteses. Ao desempilhar,
verifique se o topo da pilha é um abre parênteses. Se a expressão estiver
correta, sua pilha estará vazia no final.'''

par = input("Digite uma sequencia de parênteses: ")
pilha = []

for i in par:
    if i == '(':
        pilha.append(i)

    elif i == ')':
        if not pilha:
            pilha.append(i)
        else:
            pilha.pop()

if not pilha:
    print('OK. Parenteses devidamente fechados!')
else:
    print('ERRO. Os Parenteses não foram devidamente abertos ou fechados!')
    