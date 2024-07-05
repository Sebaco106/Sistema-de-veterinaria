# Sistema de Veterinaria - Pruebas de Software

Este repositorio contiene ejemplos y pruebas relacionadas con el desarrollo de software para un sistema de gestión veterinaria. A continuación, se presentan algunos conceptos clave y técnicas de prueba utilizadas en este contexto.

## Conceptos del Sistema de Veterinaria

El sistema de veterinaria está diseñado para gestionar pacientes y servicios veterinarios, incluyendo:

- Registro de pacientes y mascotas.
- Gestión de citas y turnos para consultas y procedimientos.
- Gestión de inventario de medicamentos, insumos y equipo veterinario.
- Gestión de facturación y cobro de servicios veterinarios.

## Técnicas de Prueba Utilizadas

### Partición de Equivalencia

La partición de equivalencia se utiliza para dividir el conjunto de datos en clases o grupos equivalentes, probando un único valor de cada clase para reducir la redundancia de pruebas.

### Valores Límite

La prueba de valores límite evalúa los límites extremos de los datos de entrada y salida del sistema, buscando identificar errores en los límites críticos como desbordamientos de memoria o cálculos incorrectos.

### Transición de Estado

Las pruebas de transición de estado evalúan cómo el sistema responde a los cambios de estado, como pasar de una pantalla de registro de paciente a la gestión de citas, asegurando que la transición sea fluida y correcta.

### Tablas de Decisión

Las tablas de decisión ayudan a definir el comportamiento del sistema en diferentes condiciones de entrada, especificando las acciones que deben tomarse según combinaciones específicas de factores y condiciones.

## Ejemplos en Este Repositorio

- **test_particion_equivalencia.py**: Ejemplos de pruebas utilizando partición de equivalencia.
- **test_valores_limite.py**: Ejemplos de pruebas utilizando valores límite.
- **mostrar_transicion_estado.py**: Visualización gráfica de transiciones de estado del sistema.

Cada archivo de prueba está diseñado para demostrar cómo se pueden aplicar estas técnicas en el contexto del desarrollo de software para sistemas veterinarios.
