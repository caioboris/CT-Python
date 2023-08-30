def busca(vet,x):
    #(list,double) -> int
    i = 0
    while i < len(vet) and vet[i] != x:
        i = i + 1
    if i == len(vet):
        return -1
    else:
        return i

vet = [57,100,49,73,-23]
x = 73

def buscaFor(vet,x):
    for i in range(len(vet)):
        if vet[i] == x:
            return i
    return -1

print(busca(vet,x))
print(buscaFor(vet,x))