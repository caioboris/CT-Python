# Escreva um programa que declara uma matriz 5x7 de números inteiros e preenche todos os
# valores com números aleatórios no intervalo de 0 a 1000.

import random

matrizA = []
i = 0

linhas = 5
colunas = 7

#iniciando a matriz com 0
while i < linhas:
    matrizA.append([0] * colunas)
    i = i+ 1
    
#Preenchendo a matriz com números aleatórios entre 0 e 1000
for i in range(linhas):
    for j in range(colunas):
        matrizA[i][j] = random.randint(0,1000)
        
#Imprimindo a matriz

for i in range(linhas):
    for j in range(colunas):
        print(matrizA[i][j], end = "\t")
    print()