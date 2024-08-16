ages = []
for i in range(10):
    while True:
        try:
            age = int(input(f"Ingresa la edad de la persona {i+1}: "))
            if age < 0:
                print("La edad no puede ser negativa. Intente nuevamente.")
            else:
                ages.append(age)
                break
        except ValueError:
            print("La edad debe ser un número entero. Intente nuevamente.")

age = tuple(ages)

count = 0
for age in ages:
    if age > 20:
        count += 1

print(f"La cantidad de personas con edades superiores a 20 es: {count}")