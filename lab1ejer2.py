def max_de_tres(a, b, c):
    """
    Devuelve el mayor de tres números.

    Args:
        a (int o float): Primer número.
        b (int o float): Segundo número.
        c (int o float): Tercer número.

    Returns:
        int o float: El mayor de los tres números.
    """
    if a >= b and a >= c:
        return a 
    elif b >= a and b >= c:
        return b
    else:
        return c 
valor = max_de_tres(1, 2, 3)
print('El número mayor es: ', valor)