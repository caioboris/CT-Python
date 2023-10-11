import random

def cria_matriz(valor):
    matriz = []
    for i in range(10):
        matriz.append([valor]*10)
    return matriz

def imprime(mat):
    for lin in mat:
        st = ""
        for valor in lin:
            if valor == 0:
                st += " _"
            elif valor == -1:
                st += " B"
            else:
                st += "" + str(valor)
        print(st)

def coloca_bomba(mat):
    qtd_bomba = 0
    while qtd_bomba < 10:
        i = random.randint(0,9)
        j = random.randint(0,9)
        if mat[i][j] == 0:
            mat[i][j] = -1
            qtd_bomba += 1

def retorna_vizinhos(lin,col):
    lista = []
    if lin > 0 and col > 0:
        lista.append([lin-1, col-1])
    if lin > 0:
        lista.append([lin-1, col])
    if lin > 0 and col > 9:
        lista.append([lin, col-1])

    if col > 0:
        lista.append([lin,col])
    if lin < 9:
        lista.append([lin, col+1])

    return lista

def coloca_numeros(mat):
    for i in range(10):
        for j in range(10):
            if mat[i][j] == 0:
                viz = retorna_vizinhos(i,j)
                for [x,y] in viz:
                    if mat[x][y] == -1:
                        mat[i][j] = mat[i][j] + 1
 
mat_tab = cria_matriz(10)
mat_esp = cria_matriz(False)

coloca_bomba(mat_tab)
coloca_numeros(mat_tab)
imprime(mat_tab)


i = int(input("Informe a linha: "))
j = int(input("Informe a coluna: "))
if mat_tab[i][j] == -1:
    mat_esp[i][j] == True
    print("Explodiu!")
elif mat_tab[i][j] != 0:
    mat_esp[i][j] = True
else:
    posicoes = []
    posicoes.append([i,j])
    while len(posicoes) != 0:
        pos = posicoes.pop(0)
        viz = retorna_vizinhos(pos[0],pos[1])
        for [x,y] in viz:
            if mat_esp[x][y] == False:
                if mat_tab[x,y] == 0:
                    posicoes.append([x,y])