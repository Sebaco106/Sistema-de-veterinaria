import unittest
from veterinaria import Paciente, SistemaVeterinario

class TestValoresLimite(unittest.TestCase):
    def setUp(self):
        self.sistema = SistemaVeterinario()

    def test_edades_limite(self):
        paciente_joven = Paciente(1, "Ana Lopez", "Max", "Perro", "Beagle", 0, "Recien nacido")
        paciente_viejo = Paciente(2, "Carlos Ruiz", "Bella", "Gato", "Siames", 20, "Gato senior")
        self.sistema.registrar_paciente(paciente_joven)
        self.sistema.registrar_paciente(paciente_viejo)
        self.assertEqual(self.sistema.obtener_paciente(1).edad, 0)
        self.assertEqual(self.sistema.obtener_paciente(2).edad, 20)

    def test_inventario_limite(self):
        self.sistema.agregar_inventario("Vacuna antirrábica", 1)
        self.assertEqual(self.sistema.obtener_inventario()["Vacuna antirrábica"], 1)

if __name__ == "__main__":
    unittest.main()
