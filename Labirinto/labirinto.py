def lista_vizinhos(i, j, linhas, colunas):
    resp = []
    #cima
    if i > 0:
        resp.append([i-1, j])
    #esquerda
    if j > 0:
        resp.append([i, j-1])
    #direita    
    if j < colunas - 1:
        resp.append([i, j+1])
    #baixo
    if i < linhas - 1:
        resp.append([i+1, j])

    return resp                


matriz = []
matriz.append([0, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0])
matriz.append([0, -1, 0, 0, -1, 0, -1, 0, -1, -1, 0])
matriz.append([0, 0, -1, 0, -1, 0, -1, 0, 0, 0, -1])
matriz.append([0, -1, 0, -1, 0, 0, 0, -1, -1, 0, 0])
matriz.append([0, 0, 0, -1, 0, -1, 0, 0, 0, -1, 0])
matriz.append([0, -1, 0, 0, 0, 0, 0, 0, -1, 0, 0])

ini = [0, 0]
fim = [5, 10]

lista = []
lista.append(ini)
matriz[0][0] = 1

while len(lista) != 0:
    [x, y] = lista.pop(0)
    valor = matriz[x][y] + 1
    vizinhos = lista_vizinhos(x, y, 6, 11)
    for [i, j] in vizinhos:
        if matriz[i][j] == 0:
            lista.append([i, j])
            matriz[i][j] = valor

for lin in matriz:
    print(lin)