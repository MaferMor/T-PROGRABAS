a = 3
b = 4

print(a + b)
resultado1 = a + b 

c = int(input("Ingresa un número: "))
if c % 2 == 0:
    resultado2 = c * 2
else:
    resultado2 = c * 3
print("El resultado es:", resultado2)


def multiplicar(x, y):
    return x * y
resultado3 = multiplicar(5, 6)
print("El resultado es:", resultado3)


resultado4 = 0
for i in range(1, 6):
    resultado4 += i
print("La suma total es:", resultado4)


lista = [1, 2, 3, 4, 5]
resultado5 = [x * 2 for x in lista]
print("La lista resultado5 es:", resultado5)


d = int(input("Ingresa un número: "))
try:
    resultado6 = 10 / d
    print("El resultado de la división es:", resultado6)
except ZeroDivisionError:
    print("Error: división por cero no permitida.")


persona = {
    "nombre": "Ana",
    "edad": 25,
    "profesión": "Ingeniera"
}
resultado7 = persona["edad"]
print("La edad de Ana es:", resultado7)


cadena = input("Ingresa una cadena de texto: ")
cadena_mayusculas = cadena.upper()
resultado8 = len(cadena_mayusculas)
print("La cadena en mayúsculas es:", cadena_mayusculas)
print("La longitud de la cadena es:", resultado8)


cuadrado = lambda x: x ** 2
resultado9 = cuadrado(7)
print("El cuadrado de 7 es:", resultado9)

lista_pares = [x for x in range(1, 11) if x % 2 == 0]
resultado10 = sum(lista_pares)
print("La suma de los números pares entre 1 y 10 es:", resultado10)
 
total = resultado1 + resultado2 + resultado3 + resultado4 + sum(resultado5) + resultado6 + resultado7 + resultado8 + resultado9 + resultado10
print("El resultado final es:", total)