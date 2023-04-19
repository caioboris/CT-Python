# def aumento(valor, percentual):
#     novoValor = (1 + percentual / 100) * valor
#     return novoValor

# resultado = aumento(350.00, 15)

def divisao(a, b):
    return a // b, a % b

res = divisao(5, 3)

print(res)
print("quociente: ", res[0])
print("resto: ", res[1])