def criaTabuleiro():
    matriz = []
    matriz.append([' '] * 3)
    matriz.append([' '] * 3)
    matriz.append([' '] * 3)
    return matriz

def imprime(mat):
    for lin in mat:
        print(lin)
        
def temEspaco(mat):
    for i in range(3):
        for j in range(3):
            if mat[i][j] == ' ':
                return True
    return False

def joga(mat, lin, col, jogador):
    if mat[lin][col] == ' ':
        mat[lin][col] = jogador
        return True
    else:
        return False
    
def haGanhador(mat):
    #linha
    for i in range(3):
        if mat[i][0] == mat[i][1] and mat[i][1] == mat[i][2] and mat[i][0] != ' ':
            return True
    #coluna
    for j in range(3):
        if mat[i][0] == mat[i][1] and mat[i][1] == mat[i][2] and mat[i][0] != ' ':
            return True
    #diagonais
    if mat[0][0] == mat[1][1] and mat[1][1] == mat[2][2] and mat[0][0] != ' ':    
        return True
    
    if mat[0][2] == mat[1][1] and mat[1][1] == mat[2][0] and mat[0][2] != ' ':
        return True
    return False


def trocaJogador(jogador: str):
    if jogador.upper == 'X':
        return 'O'
    return 'X'
