import unittest
from veterinaria import Paciente, SistemaVeterinario

class TestTablasDecision(unittest.TestCase):
    def setUp(self):
        self.sistema = SistemaVeterinario()

    def test_facturacion_decision(self):
        paciente = Paciente(1, "Juan Perez", "Rex", "Perro", "Labrador", 5, "Vacunas al día")
        self.sistema.registrar_paciente(paciente)
        self.sistema.generar_factura(1, ["Consulta general", "Vacuna antirrábica"], 150.0)
        facturas = self.sistema.obtener_facturas()
        self.assertEqual(facturas[0]["total"], 150.0)

if __name__ == "__main__":
    unittest.main()
