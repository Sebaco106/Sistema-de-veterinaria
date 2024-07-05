import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.table as table

data = {
    "Condiciones": [
        "ID válido",
        "Nombre del dueño completo",
        "Nombre de la mascota completo",
        "Especie completa",
        "Raza completa",
        "Edad mayor o igual a 0",
        "Historial médico completo"
    ],
    "Regla 1": ["Sí", "Sí", "Sí", "Sí", "Sí", "Sí", "Sí"],
    "Regla 2": ["Sí", "No", "Sí", "Sí", "Sí", "Sí", "Sí"],
    "Regla 3": ["No", "Sí", "Sí", "Sí", "Sí", "Sí", "Sí"],
    "Regla 4": ["Sí", "Sí", "No", "Sí", "Sí", "Sí", "Sí"],
    "Acción": ["Registrar", "No registrar", "No registrar", "No registrar"]
}

df = pd.DataFrame(data)

print(df)

fig, ax = plt.subplots()

ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_frame_on(False)

tabla = table.table(ax, cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

tabla.auto_set_font_size(False)
tabla.set_fontsize(12)
tabla.scale(1.2, 1.2)

plt.show()
