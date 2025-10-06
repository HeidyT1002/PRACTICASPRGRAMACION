# Tarea: Trabajo con Archivos de Texto en Python
# Autor: [Tu nombre]
# Fecha: [coloca la fecha actual]
# Descripción:
# Este programa crea un archivo de texto, escribe notas personales,
# lee su contenido línea por línea y muestra cada línea en consola.

# -----------------------------
# 1. Escritura del archivo
# -----------------------------
# Creamos (o sobrescribimos si ya existe) el archivo my_notes.txt
# usando el modo de apertura 'w' (write).
archivo = open("my_notes.txt", "w")

# Escribimos al menos tres líneas de notas personales
archivo.write("Nota 1: Hoy aprendí a manejar archivos en Python.\n")
archivo.write("Nota 2: El método write() permite escribir texto en un archivo.\n")
archivo.write("Nota 3: También puedo leer cada línea con readline().\n")

# Cerramos el archivo después de escribir
archivo.close()

# -----------------------------
# 2. Lectura del archivo
# -----------------------------
# Abrimos el archivo en modo lectura ('r')
archivo = open("my_notes.txt", "r")

# Leemos el contenido línea por línea
print("Contenido del archivo my_notes.txt:\n")

# readline() lee una línea a la vez
linea = archivo.readline()
while linea:
    # Mostramos la línea leída
    print(linea.strip())  # strip() elimina los saltos de línea al imprimir
    # Leemos la siguiente línea
    linea = archivo.readline()

# -----------------------------
# 3. Cierre del archivo
# -----------------------------
archivo.close()
print("\nArchivo cerrado correctamente.")
