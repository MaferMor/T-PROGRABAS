def superposicion(lista1, lista2):
    """
    Devuelve True si las dos listas tienen al menos un miembro en común, False en caso contrario.

    Args:
        lista1 (list): Primera lista.
        lista2 (list): Segunda lista.

    Returns:
        bool: True si las listas tienen al menos un miembro en común, False en caso contrario.
    """
    for elemento1 in lista1:
        for elemento2 in lista2:
            if elemento1 == elemento2:
                return True
    return False
print(superposicion([1, 2, 3], [2, 4, 5]))