import random

numero_secreto = random.randint(1, 100)

print("¡Bienvenido al juego de adivinanza!")
print("Estoy pensando en un número entre 1 y 100.")

intentos = 0

while True:
    respuesta = int(input("¿Cuál es tu apuesta? "))
    intentos += 1
    if respuesta == numero_secreto:
        print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
        break
    elif respuesta < numero_secreto:
        print("Tu apuesta es demasiado baja. Intenta de nuevo.")
    else:
        print("Tu apuesta es demasiado alta. Intenta de nuevo.")