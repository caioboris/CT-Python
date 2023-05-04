
pessoasEntrevistadas = 100
i = 0
salarioTotal = 0
maiorIdade = 0 
mulheresAte3000 = 0
menorIdade = 150

while i < pessoasEntrevistadas:
    idade = int(input("Informe sua idade: "))
    sexo = input("Informe seu sexo (M/F): ")
    salario = float(input("Informe seu salario: "))
    
    salarioTotal += salario
    
    if idade > maiorIdade:
        maiorIdade = idade
    if idade < menorIdade:
        menorIdade = idade
    
    if sexo == "F" and salario <= 3000:    
        mulheresAte3000 += 1

    i +=1

def mediaSalarial(salario):
    return salario // 100


print(f"Média salarial: {mediaSalarial(salarioTotal)}")
print(f"Maior Idade: {maiorIdade}")
print(f"Menor Idade: {menorIdade}")
print(f"Mulheres que recebem ate 3000: {mulheresAte3000}")