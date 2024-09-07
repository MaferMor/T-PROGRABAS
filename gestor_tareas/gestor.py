class GestorTareas:
    def __init__(self):
        self.tareas = []
        self.id_actual = 1

    def agregar_tarea(self, nombre):
        tarea = {'id': self.id_actual, 'nombre': nombre, 'completada': False}
        self.tareas.append(tarea)
        self.id_actual += 1
        print(f"Tarea '{nombre}' agregada con éxito.")

    def listar_tareas(self):
        if not self.tareas:
            print("No hay tareas.")
        else:
            print("\nListado de Tareas:")
            for tarea in self.tareas:
                estado = "Completada" if tarea['completada'] else "Pendiente"
                print(f"ID: {tarea['id']}, Nombre: {tarea['nombre']}, Estado: {estado}")

    def eliminar_tarea(self, id_tarea):
        tarea = next((t for t in self.tareas if t['id'] == id_tarea), None)
        if tarea:
            self.tareas.remove(tarea)
            print(f"Tarea ID {id_tarea} eliminada con éxito.")
        else:
            print("Tarea no encontrada.")

    def marcar_completada(self, id_tarea):
        tarea = next((t for t in self.tareas if t['id'] == id_tarea), None)
        if tarea:
            tarea['completada'] = True
            print(f"Tarea ID {id_tarea} marcada como completada.")
        else:
            print("Tarea no encontrada.")