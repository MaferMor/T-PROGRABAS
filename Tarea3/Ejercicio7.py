numeros = input("Ingrese la lista de números separados por comas: ")

numeros_lista = [int(x) for x in numeros.split(",")]

suma = sum(numeros_lista)

print("La suma de los números es:", suma)