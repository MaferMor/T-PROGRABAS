import unittest
from gestor import GestorTareas

class TestGestorTareas(unittest.TestCase):
    def setUp(self):
        self.gestor = GestorTareas()

    def test_agregar_tarea(self):
        self.gestor.agregar_tarea("Tarea 1")
        self.assertEqual(len(self.gestor.tareas), 1)
        self.assertEqual(self.gestor.tareas[0]['nombre'], "Tarea 1")

    def test_eliminar_tarea(self):
        self.gestor.agregar_tarea("Tarea 1")
        self.gestor.eliminar_tarea(1)
        self.assertEqual(len(self.gestor.tareas), 0)

    def test_marcar_completada(self):
        self.gestor.agregar_tarea("Tarea 1")
        self.gestor.marcar_completada(1)
        self.assertTrue(self.gestor.tareas[0]['completada'])

if __name__ == "__main__":
    unittest.main()