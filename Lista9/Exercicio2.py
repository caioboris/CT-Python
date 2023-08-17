# Escreva uma função getDimensao que recebe como parâmetro uma matriz mat de números
# reais (double) e retorna uma tupla (ou uma lista) de inteiros contendo o número de linhas e
# o número de colunas de mat. Note que, sua tupla terá duas posições.


def getDimensao(mat):
    linhas = len(mat)
    colunas = len(mat[0])
    return (linhas, colunas)

matrizA = []
i = 0

while i < 5:
    matrizA.append([244.2] * 7)
    i = i+ 1
    
print(getDimensao(matrizA))