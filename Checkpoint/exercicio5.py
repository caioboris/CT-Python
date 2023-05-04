salario = int(input("Informe o salário: "))

taxa1 = 1100.00
taxa2 = 2203.48
taxa3 = 3305.23
taxa4 = 6433.57 

def verificaAliquota(salario):
    contador = 0.0
    
    if taxa3 < salario < taxa4:
        contador += (salario - taxa3) * 0.14
    if taxa2 < salario < taxa3 or salario > taxa3:
        contador += (taxa3 - taxa2) * 0.12
    if taxa1 < salario < taxa2 or salario > taxa2:
        contador += (taxa2 - taxa1) * 0.09
    contador += (taxa1 * 0.075)
    
    return contador
    
print(f"Desconto do INSS {verificaAliquota(salario)}")
        
    