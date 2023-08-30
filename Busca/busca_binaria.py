def buscaBinario(vet,x):
    inicio = 0
    fim = len(vet) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if(vet[meio] > x):
            