def potencia(a, b):
    if b == 0:
        print(f"{a}^0 = 1")
        return 1
    else:
        print(f"Calculando {a}^{b} = {a} * {a}^{b-1}")
        result = a * potencia(a, b - 1)
        print(f"{a}^{b} = {result}")
        return result
potencia(2, 3)
