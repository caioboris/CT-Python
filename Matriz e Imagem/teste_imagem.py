import Imagem as img

dados = img.getMatrizImagemColorida("./resources/processamentoImagens/naturezaMorta.jpg")

matrizR = dados[0]
matrizG = dados[1]
matrizB = dados[2]

lin = len(matrizR)
col = len(matrizR[0])
print(lin, " x ", col)

for i in range(lin):
    for j in range(col):
        if matrizR[i][j] == 10 and matrizG[i][j] == 30 and matrizB[i][j] == 91:
            matrizR[i][j] = 255
            matrizG[i][j] = 255
            matrizB[i][j] = 255

img.salvaImagemColorida("./resources/processamentoImagens/nat2.jpg", matrizR, matrizG, matrizB)

