import unittest
from veterinaria import Paciente, SistemaVeterinario

class TestParticionEquivalencia(unittest.TestCase):
    def setUp(self):
        self.sistema = SistemaVeterinario()

    def test_registrar_paciente_valido(self):
        paciente = Paciente(1, "Juan Perez", "Rex", "Perro", "Labrador", 5, "Vacunas al día")
        resultado = self.sistema.registrar_paciente(paciente)
        self.assertTrue(resultado)
        self.assertEqual(self.sistema.obtener_paciente(1), paciente)

    def test_registrar_paciente_invalido(self):
        paciente = Paciente(None, "", "", "", "", -1, "")
        resultado = self.sistema.registrar_paciente(paciente)
        self.assertFalse(resultado)
        self.assertIsNone(self.sistema.obtener_paciente(None))

    def test_agendar_cita_valida(self):
        self.sistema.agendar_cita(1, "2023-08-15", "Consulta general")
        self.assertEqual(len(self.sistema.obtener_citas()), 1)

    def test_agendar_cita_invalida(self):
        self.sistema.agendar_cita(None, "", "")
        self.assertEqual(len(self.sistema.obtener_citas()), 1)

if __name__ == "__main__":
    unittest.main()
