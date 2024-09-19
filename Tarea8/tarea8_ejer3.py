def invertir_cadena(cadena):
    if len(cadena) == 0:
        print("Cadena vacía, devolviendo cadena vacía.")
        return ""
    elif len(cadena) == 1:
        print(f"Cadena con un solo carácter '{cadena}', devolviendo '{cadena}'.")
        return cadena
    else:
        print(f"Invirtiendo '{cadena[1:]}' y agregando '{cadena[0]}' al final.")
        return invertir_cadena(cadena[1:]) + cadena[0]
invertir_cadena("hola")
