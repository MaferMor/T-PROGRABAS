nombre_archivo = input("Ingrese el nombre del archivo de texto: ")

try:
    with open(nombre_archivo, "r") as archivo:
        # Leer el contenido del archivo
        contenido = archivo.read()
        # Imprimir el contenido del archivo
        print(contenido)
except FileNotFoundError:
    print("El archivo no existe")
except Exception as e:
    print("Error al leer el archivo:", e)

    