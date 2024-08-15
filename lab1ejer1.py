def max(a, b):
    """
    Devuelve el mayor de dos números.

    Args:
        a (int o float): Primer número.
        b (int o float):Segundo número.
    
    Returns:
        int o float: El mayor de los números.
    """
    if a > b:
        return a 
    else:
        return b
valor = max(2,10)
print('El numero mas grande es ',valor)