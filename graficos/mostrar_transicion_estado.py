from graphviz import Digraph

# Crear un objeto Digraph
dot = Digraph(comment='Diagrama de Transición de Estados - Sistema de Veterinaria')

# Definir los estados
states = ['Inicio', 'Registrar Paciente', 'Gestión de Citas', 'Gestión de Inventario', 'Gestión de Facturación', 'Salir']

# Añadir nodos para los estados
for state in states:
    dot.node(state, state)

# Definir las transiciones
transitions = [
    ('Inicio', 'Registrar Paciente'),
    ('Registrar Paciente', 'Gestión de Citas'),
    ('Gestión de Citas', 'Gestión de Inventario'),
    ('Gestión de Inventario', 'Gestión de Facturación'),
    ('Gestión de Facturación', 'Salir'),
]

# Añadir transiciones a la gráfica
for transition in transitions:
    dot.edge(transition[0], transition[1])

# Renderizar y mostrar el diagrama de estados
dot.render('transicion_estado_veterinaria', format='png', view=True)
