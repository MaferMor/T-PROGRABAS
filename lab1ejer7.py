def es_palindromo(palabra):
    """
    Devuelve True si la palabra es un palíndromo, False en caso contrario.

    Args:
        palabra (str): Palabra a verificar.

    Returns:
        bool: True si la palabra es un palíndromo, False en caso contrario.
    """
    return palabra == palabra[::-1]


def es_palindromo(palabra):
    return palabra == palabra[::-1]
print(es_palindromo("radar"))