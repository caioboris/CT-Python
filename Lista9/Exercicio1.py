# Crie a matriz do jogo da velha abaixo e faça a impressão na tela:
# x o x
# o x 
# o x x


tabuleiro = []

i = 0

while i < 3:
    tabuleiro.append([' '] * 3)
    i = i +1
    
tabuleiro[0][0] = 'x'
tabuleiro[1][0] = 'o'
tabuleiro[2][0] = 'x'
tabuleiro[0][1] = 'x'
tabuleiro[0][2] = 'x'
tabuleiro[1][1] = 'x'
tabuleiro[2][2] = 'x'

for linha in tabuleiro:
    print(linha)