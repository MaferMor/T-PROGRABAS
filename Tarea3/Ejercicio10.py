n_calificaciones = int(input("Ingrese el número de calificaciones: "))

suma_calificaciones = 0

for i in range(n_calificaciones):
    calificacion = float(input(f"Ingrese la calificación {i+1}: "))
    suma_calificaciones += calificacion

promedio = suma_calificaciones / n_calificaciones

print(f"El promedio es: {promedio:.2f}")
