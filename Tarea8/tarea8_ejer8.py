def busqueda_binaria(lista, objetivo, inicio=0, fin=None):
    if fin is None:
        fin = len(lista) - 1

    if inicio > fin:
        print(f"{objetivo} no se encuentra en la lista.")
        return False

    medio = (inicio + fin) // 2
    print(f"Buscando {objetivo} entre {lista[inicio:fin+1]}, medio: {lista[medio]}")

    if lista[medio] == objetivo:
        print(f"¡Encontrado! {objetivo} está en la posición {medio}.")
        return True
    elif lista[medio] > objetivo:
        return busqueda_binaria(lista, objetivo, inicio, medio - 1)
    else:
        return busqueda_binaria(lista, objetivo, medio + 1, fin)

lista = [3, 9, 10, 27, 38, 43, 82]
objetivo = 27
print(f"Lista: {lista}")
resultado = busqueda_binaria(lista, objetivo)
