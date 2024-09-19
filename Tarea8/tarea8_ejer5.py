def suma_digitos(n):
    if n < 10:
        print(f"Último dígito encontrado: {n}")
        return n
    else:
        print(f"Sumando el dígito {n % 10} de {n} y llamando a suma_digitos({n // 10})")
        result = n % 10 + suma_digitos(n // 10)
        print(f"Suma parcial para {n} = {result}")
        return result
suma_digitos (1234)