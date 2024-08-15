def longitud(elemento):
    """
    devuelve a longitud de una lista o una cadena

    Args:
        elemento (list o str): Lista o cadena de la que se quiere calcular la lontitud.

    Returns:
        int: la longitud de la lista o cadena.
    """
    contador = 0
    for _ in elemento:
        contador += 1
    return contador 


