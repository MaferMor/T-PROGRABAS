numero = int(input("Ingrese un número: "))

print("Tabla de multiplicar del", numero)
print("------------------------")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
    