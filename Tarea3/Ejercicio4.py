import datetime

dia_nacimiento = int(input("Ingrese el día de su nacimiento: "))
mes_nacimiento = int(input("Ingrese el mes de su nacimiento: "))
anio_nacimiento = int(input("Ingrese el año de su nacimiento: "))

fecha_nacimiento = datetime.date(anio_nacimiento, mes_nacimiento, dia_nacimiento)

fecha_actual = datetime.date.today()

diferencia = fecha_actual - fecha_nacimiento

print(f"Han pasado {diferencia.days} días desde su nacimiento")
