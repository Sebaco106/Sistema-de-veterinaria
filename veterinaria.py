class Paciente:
    def __init__(self, id_paciente, nombre_dueño, nombre_mascota, especie, raza, edad, historial_medico):
        self.id_paciente = id_paciente
        self.nombre_dueño = nombre_dueño
        self.nombre_mascota = nombre_mascota
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.historial_medico = historial_medico

class SistemaVeterinario:
    def __init__(self):
        self.pacientes = {}
        self.citas = []
        self.inventario = {}
        self.facturas = []

    def registrar_paciente(self, paciente):
        if (paciente.id_paciente is None or
                not paciente.nombre_dueño or
                not paciente.nombre_mascota or
                not paciente.especie or
                not paciente.raza or
                paciente.edad < 0 or
                not paciente.historial_medico):
            return False
        self.pacientes[paciente.id_paciente] = paciente
        return True
    
    def obtener_paciente(self, id_paciente):
        return self.pacientes.get(id_paciente)

    def agendar_cita(self, id_paciente, fecha, procedimiento):
        self.citas.append({
            "id_paciente": id_paciente,
            "fecha": fecha,
            "procedimiento": procedimiento
        })
    
    def obtener_citas(self):
        return self.citas

    def agregar_inventario(self, item, cantidad):
        if item in self.inventario:
            self.inventario[item] += cantidad
        else:
            self.inventario[item] = cantidad

    def obtener_inventario(self):
        return self.inventario

    def generar_factura(self, id_paciente, items, total):
        self.facturas.append({
            "id_paciente": id_paciente,
            "items": items,
            "total": total
        })
    
    def obtener_facturas(self):
        return self.facturas

if __name__ == "__main__":
    sistema = SistemaVeterinario()
    
    paciente1 = Paciente(1, "Juan Perez", "Rex", "Perro", "Labrador", 5, "Vacunas al día")
    sistema.registrar_paciente(paciente1)
    
    sistema.agendar_cita(1, "2023-08-15", "Consulta general")
    
    sistema.agregar_inventario("Vacuna antirrábica", 10)
    
    
    sistema.generar_factura(1, ["Consulta general", "Vacuna antirrábica"], 150.0)
    
    print(sistema.obtener_paciente(1))
    print(sistema.obtener_citas())
    print(sistema.obtener_inventario())
    print(sistema.obtener_facturas())
