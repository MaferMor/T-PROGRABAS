def generar_n_caracteres(n, caracter):
    """
    Devuelve una cadena que consiste en el caracter multiplicado por n.

    Args:
        n (int): Número de veces que se debe repetir el caracter.
        caracter (str): Caracter a repetir.

    Returns:
        str: Cadena que consiste en el caracter multiplicado por n.
    """
    return caracter * n
print(generar_n_caracteres(3, "a"))