# Usando a função do exercício anterior, escreva um programa que imprime os 100 primeiros
# números primos começando do número 2


def ePrimo(num):
    i = 2
    if num == 1: return False
    
    while i <= num:
        if(num % i != 0):
            i += 1
        else:
            if(i == num):
                return True
            else:
                return False
            
contador = 0
n = 1

while contador < 10000:
    if(ePrimo(n)):
        print(n)
        contador += 1
    n += 1
    
    
            
            