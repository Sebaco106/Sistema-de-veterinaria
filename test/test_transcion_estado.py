import unittest
from veterinaria import Paciente, SistemaVeterinario

class TestTransicionEstado(unittest.TestCase):
    def setUp(self):
        self.sistema = SistemaVeterinario()
        self.paciente = Paciente(1, "Juan Perez", "Rex", "Perro", "Labrador", 5, "Vacunas al día")
        self.sistema.registrar_paciente(self.paciente)

    def test_transicion_estado_paciente(self):
        self.paciente.historial_medico = "Consulta general realizada"
        self.sistema.registrar_paciente(self.paciente)
        self.assertEqual(self.sistema.obtener_paciente(1).historial_medico, "Consulta general realizada")

    def test_transicion_estado_inventario(self):
        self.sistema.agregar_inventario("Vacuna antirrábica", 10)
        self.sistema.agregar_inventario("Vacuna antirrábica", -2)
        self.assertEqual(self.sistema.obtener_inventario()["Vacuna antirrábica"], 8)

if __name__ == "__main__":
    unittest.main()
