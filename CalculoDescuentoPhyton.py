# Archivo: CalculoDescuentoPython.py

def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento en una compra.

    Parámetros:
    monto_total (float): El monto total de la compra.
    porcentaje_descuento (float, opcional): El porcentaje de descuento a aplicar. Por defecto es 10%.

    Retorna:
    float: El monto del descuento.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Programa principal
# Primera llamada: usando el valor predeterminado del descuento (10%)
monto1 = 150.0
descuento1 = calcular_descuento(monto1)
total_a_pagar1 = monto1 - descuento1

print(f"Compra 1: Monto total: ${monto1:.2f}")
print(f"Descuento aplicado: ${descuento1:.2f}")
print(f"Monto a pagar: ${total_a_pagar1:.2f}\n")

# Segunda llamada: especificando un porcentaje de descuento diferente
monto2 = 200.0
descuento2 = calcular_descuento(monto2, 20)  # 20% de descuento
total_a_pagar2 = monto2 - descuento2

print(f"Compra 2: Monto total: ${monto2:.2f}")
print(f"Descuento aplicado: ${descuento2:.2f}")
print(f"Monto a pagar: ${total_a_pagar2:.2f}")
