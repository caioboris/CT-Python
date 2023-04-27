# Escreva uma função que recebe duas Strings: frase e letras; a frase representa um
# conjunto de caracteres e letras alguns caracteres. Sua função deverá substituir cada
# caracter c contido na frase pelo caracter * se este caracter c estiver presente em letras.
# Por exemplo, se a frase for:


def changeCharacter(frase, letra):
    resp = ""
    i = 0
    for c in frase:
        if(c in letra):
            resp += "*"
        else:
            resp += c
    return resp



teste = changeCharacter("my dad is a great software developer", "ae")
print(teste)