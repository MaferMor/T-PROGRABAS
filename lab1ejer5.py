def suma(lista):
    total = 0
    for numero in lista:
        total += numero
    return total

def multip(lista):
    resultado = 1
    for numero in lista:
        resultado *= numero
    return resultado

print(suma([1, 2, 3, 4]))

print(multip([1, 2, 3, 4]))