names = ["Ana", "Pedro", "Alicia", "Andrés", "Beatriz", "Alejandro", "Carlos", "Adriana", "Elena", "Francisco"]

letter = input("Ingresa la letra a buscar: ").lower()

count = 0

for name in names:
    if name[0].lower() == letter:
        count += 1
print(f"La cantidad de nombres que comienzan con la letra '{letter}' es: {count}")