# Dados duas strings (um contendo uma frase e outro contendo uma palavra), determine o
# número de vezes que a palavra ocorre na frase. Exemplo: Para a palavra ANA e a frase:
# ANA E MARIANA GOSTAM DE BANANA
# Temos que a palavra ocorre 4 vezes na frase. Escreva um programa que resolve o problema
# acima, seu programa deverá receber as duas strings e retornar o número de ocorrências da
# palavra na frase.

def wordCount(frase, palavra):
    frase = frase.upper()
    palavra = palavra.upper()
    contador = 0
    i = 0
    while i < len(frase):
        frase.find(palavra + i)
        contador +=1
        i += 1
    return contador

teste = wordCount("ANA E MARIANA GOSTAM DE BANANA", "ANA")        

print(teste)
    