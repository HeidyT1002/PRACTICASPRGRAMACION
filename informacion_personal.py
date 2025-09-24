# Crear un diccionario con la información inicial
informacion_personal = {
    "nombre": "Ana Pérez",
    "edad": 28,
    "ciudad": "Quito",
    "profesion": "Ingeniera"
}

# Modificar la ciudad directamente
informacion_personal.update({"ciudad": "Guayaquil"})

# Agregar una profesión secundaria (o cualquier otra información relevante)
informacion_personal.update({"profesion_secundaria": "Fotografía"})

# Verificar existencia de la clave "telefono" y agregarla si no existe
informacion_personal.setdefault("telefono", "0991234567")
# setdefault agrega la clave con el valor solo si no existía previamente

# Eliminar la clave "edad"
informacion_personal.pop("edad", None)
# pop elimina la clave; el segundo parámetro evita error si no existe

# Imprimir el diccionario final
print(informacion_personal)
