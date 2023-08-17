# Escreva uma função somaPos que recebe uma matriz de números inteiros e retorna um
# número inteiro que representa a soma de todos os elementos positivos existentes na matriz.

def somaPos(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] > 0:
                soma = soma + matriz[i][j]
    return soma 
                
matrizA = [
    [3, -2, 1, 0, -5],
    [7, 8, -9, 10, -4],
    [-1, 6, 0, -3, 2]
]

resultado = somaPos(matrizA)
print("Soma dos itens na matriz: ", resultado)


    