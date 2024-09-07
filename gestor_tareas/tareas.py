from gestor import GestorTareas

def mostrar_menu():
    print("\nGestor de Tareas")
    print("1. Listar tareas")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Marcar tarea como completada")
    print("5. Salir")

def main():
    gestor = GestorTareas()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            gestor.listar_tareas()
        elif opcion == '2':
            nombre_tarea = input("Ingrese el nombre de la tarea: ")
            gestor.agregar_tarea(nombre_tarea)
        elif opcion == '3':
            id_tarea = int(input("Ingrese el ID de la tarea a eliminar: "))
            gestor.eliminar_tarea(id_tarea)
        elif opcion == '4':
            id_tarea = int(input("Ingrese el ID de la tarea a marcar como completada: "))
            gestor.marcar_completada(id_tarea)
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()