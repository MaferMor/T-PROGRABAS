numero1 = int(input("Ingresa el primer número entero: "))

numero2 = int(input("Ingresa el segundo número entero: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

if numero2 != 0:
    division = numero1 / numero2
else:
    division = "Error: División por cero no permitida"


print(f"La suma de {numero1} y {numero2} es {suma}")
print(f"La resta de {numero1} y {numero2} es {resta}")
print(f"La multiplicación de {numero1} y {numero2} es {multiplicacion}")
print(f"La división de {numero1} entre {numero2} es {division}")