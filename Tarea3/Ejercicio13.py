nombres = input("Ingrese una lista de nombres separados por comas: ")

nombres_lista = [nombre.strip() for nombre in nombres.split(",")]

nombres_lista.sort()

print("La lista de nombres ordenada alfabéticamente es:")
for nombre in nombres_lista:
    print(nombre)