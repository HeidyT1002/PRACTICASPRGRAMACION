# Importamos librerías
import random

# Datos de ejemplo
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 2  # Número de semanas

# Crear matriz 3D: [ciudad][día][semana] con temperaturas aleatorias entre 15 y 35 grados
temperaturas = [[[random.randint(15, 35) for _ in range(semanas)] for _ in dias] for _ in ciudades]

# Mostrar la matriz (opcional)
print("Matriz de temperaturas (ciudad x día x semana):")
for i, ciudad in enumerate(ciudades):
    print(f"{ciudad}: {temperaturas[i]}")

# Calcular promedio por ciudad y semana
for i, ciudad in enumerate(ciudades):
    for s in range(semanas):
        suma = 0
        for d in range(len(dias)):
            suma += temperaturas[i][d][s]
        promedio = suma / len(dias)
        print(f"Promedio de temperaturas en {ciudad} - Semana {s+1}: {promedio:.2f}°C")
