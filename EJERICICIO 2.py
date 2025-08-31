# Definimos una matriz 3x3
matriz = [
    [9, 2, 7],
    [4, 6, 1],
    [3, 8, 5]
]

# Función para ordenar una fila usando Bubble Sort
def ordenar_fila(matriz, fila):
    n = len(matriz[fila])
    for i in range(n):
        for j in range(0, n-i-1):
            if matriz[fila][j] > matriz[fila][j+1]:
                # Intercambiamos elementos
                matriz[fila][j], matriz[fila][j+1] = matriz[fila][j+1], matriz[fila][j]

# Mostramos la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Elegimos la fila que queremos ordenar (por ejemplo, fila 1)
fila_a_ordenar = 1
ordenar_fila(matriz, fila_a_ordenar)

# Mostramos la matriz con la fila ordenada
print("\nMatriz después de ordenar la fila", fila_a_ordenar, ":")
for fila in matriz:
    print(fila)
