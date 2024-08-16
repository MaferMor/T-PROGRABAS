def binary_to_integer():
    binary_input = input("Escriba un número binario: ")
    try:
        integer_output = int(binary_input, 2)
        print(f"El número binario {binary_input} is igual al número entero {integer_output}.")
    except ValueError:
        print("Número binario no válido. Ingrese un número que consista únicamente en 0 y 1.")

binary_to_integer()