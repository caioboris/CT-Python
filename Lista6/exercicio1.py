# . Crie uma função em Python que recebe uma String e retorna uma outra String com os
# mesmos caracteres só que em caixa alta. Por exemplo: se a palavra for "Melancia", sua
# função deverá retornar "MELANCIA".

def toUpper(txt):
    return txt.upper()

palavra = input("Escolha uma palavra para colocar em CAIXA ALTA: ")
print(toUpper(palavra))