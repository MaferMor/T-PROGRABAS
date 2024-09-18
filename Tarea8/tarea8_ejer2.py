def fibonacci(n):
    if n == 0:
        print(f"Fibonacci({n}) = 0")
        return 0
    elif n == 1:
        print(f"Fibonacci({n}) = 1")
        return 1
    else:
        print(f"Calculando Fibonacci({n}), llamando a Fibonacci({n-1}) y Fibonacci({n-2})")
        result = fibonacci(n - 1) + fibonacci(n - 2)
        print(f"Fibonacci({n}) = {result}")
        return result
fibonacci(5)
