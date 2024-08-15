def es_vocal(caracter):
    """
    Devuelve True si el carácter es una vocal, de lo contrario devuelve False.

    Args:
        caracter (str): Carácter a evaluar.

    Returns:
        bool: true si el carácter es una vocal, False de lo contrario.
    """

    vocales = "aeiouAEIOU"
    return caracter in vocales

def es_vocal(caracter):
    caracter = caracter.lower()
    if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u":
        return True 
    else:
        return False 
print (es_vocal("b"))
    
def es_vocal(caracter):
    return caracter.lower() in "aeiou"
print (es_vocal("a"))

