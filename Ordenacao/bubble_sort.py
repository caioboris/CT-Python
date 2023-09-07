def subir(lista):
    i = len(lista) - 1
    while i > 0:
        if lista[i-1] > lista[i]:
            aux = lista[i]
            lista[i] = lista[i-1]
            lista[i-1] = aux
        i = i-1
        
def bubble_sort(lista):
    for i in range(len(lista)):
        subir(lista)
        
lista = [5, 6, 2, 5, 1, 0, 3, 4, 1, 8]
bubble_sort(lista)
print(lista)