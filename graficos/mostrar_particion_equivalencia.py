import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Parámetro": [
        "ID del Paciente", "ID del Paciente", "ID del Paciente",
        "Nombre del Dueño", "Nombre del Dueño",
        "Nombre de la Mascota", "Nombre de la Mascota",
        "Especie", "Especie",
        "Raza", "Raza",
        "Edad", "Edad",
        "Historial Médico", "Historial Médico"
    ],
    "Clase de Equivalencia": [
        "Válido", "Inválido", "Inválido",
        "Válido", "Inválido",
        "Válido", "Inválido",
        "Válido", "Inválido",
        "Válido", "Inválido",
        "Válido", "Inválido",
        "Válido", "Inválido"
    ],
    "Ejemplo de Valor": [
        "123", "-1", "\"ABC\"",
        "\"Juan Perez\"", "\"\"",
        "\"Rex\"", "\"\"",
        "\"Perro\"", "\"\"",
        "\"Labrador\"", "\"\"",
        "5", "-3",
        "\"Vacunas al día\"", "\"\""
    ]
}

df = pd.DataFrame(data)

print(df)

fig, ax = plt.subplots()

ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_frame_on(False)

tabla = plt.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

tabla.auto_set_font_size(False)
tabla.set_fontsize(12)
tabla.scale(1.2, 1.2)

plt.show()
