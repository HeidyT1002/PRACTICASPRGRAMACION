# Función para calcular temperaturas promedio por ciudad

def calcular_promedios_temperaturas(datos):
    """
    Calcula la temperatura promedio de cada ciudad a partir de un diccionario
    con temperaturas semanales.

    Parámetros:
    datos (dict): Un diccionario donde la clave es el nombre de la ciudad
                  y el valor es una lista de temperaturas semanales.

    Retorna:
    dict: Un diccionario con las ciudades como clave y su temperatura promedio como valor.
    """
    promedios = {}
    for ciudad, temperaturas in datos.items():
        promedio = sum(temperaturas) / len(temperaturas)
        promedios[ciudad] = promedio
    return promedios


# Ejemplo de uso con datos de 3 ciudades durante 4 semanas
datos_temperaturas = {
    "Quito": [14, 15, 13, 16],
    "Guayaquil": [28, 29, 30, 27],
    "Loja": [18, 19, 17, 20]
}

promedios = calcular_promedios_temperaturas(datos_temperaturas)

print("Promedios de temperaturas por ciudad:")
for ciudad, promedio in promedios.items():
    print(f"{ciudad}: {promedio:.2f} °C")
