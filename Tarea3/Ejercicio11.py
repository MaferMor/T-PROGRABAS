peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura ** 2)

print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")

if imc < 18.5:
    print("Usted tiene un peso bajo.")
elif imc < 25:
    print("Usted tiene un peso normal.")
elif imc < 30:
    print("Usted tiene sobrepeso.")
else:
    print("Usted tiene obesidad.")