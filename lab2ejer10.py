def es_bisiesto(year):
    """
    Determina si un año es bisiesto o no.

    Un año bisiesto es divisible por 4, pero no por 100, excepto si también es divisible por 400.

    Args:
        year (int): El año a verificar.

    Returns:
        bool: True si el año es bisiesto, False en caso contrario.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def main():
    try:
        año = int(input("Introduce un año para verificar si es bisiesto: "))
        if año < 0:
            print("Por favor, introduce un año positivo.")
        else:
            if es_bisiesto(año):
                print(f"El año {año} es bisiesto.")
            else:
                print(f"El año {año} no es bisiesto.")
    except ValueError:
        print("Entrada inválida. Por favor, introduce un número entero.")


if __name__ == "__main__":
    main()