'''14. Escreva um jogo da velha para dois jogadores. O jogo deve perguntar onde
você quer jogar e alternar entre os jogadores. A cada jogada, verifique se a
posição está livre. Verifique também quando um jogador venceu a partida.
Um jogo da velha pode ser visto como uma lista de 3 elementos, na qual
cada elemento é outra lista também com três elementos.'''

grid = [['00', '01', '02'],['10', '11', '12'], ['20', '21', '22']]

acertou = False
velha = False
erros = 0

while not acertou and not velha:

    simbolo = input('entre com "X" ou "O": ')
    linha = int(input('Em qual linha? '))
    coluna = int(input('Qual coluna? '))

    grid [linha][coluna] = simbolo

    for i, linha in enumerate(grid):
        for j, coluna in enumerate(grid[i]):
            print(grid[i][j], end= ' ')
        print()

    for i in range(0,len(grid)):
        if grid[i][0] == grid[i][1] and grid[i][1] == grid[i][2]:
            acertou = True
            break

    for j in range(0,len(grid)):
        if grid[0][j] == grid[1][j] and grid[1][j] == grid[2][j]:
            acertou = True
            break
    erros += 1
    velha = erros == 9

if acertou == True:
    print('Voce ganhou!')
else:
    print('Deu velha!')