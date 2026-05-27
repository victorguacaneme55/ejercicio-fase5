# ***
#  Fundamentos de Programación - UNAD
#  Fase 5 - Evaluación Final POA
#  Problema 3: Auditoría de Inventario

# ***
# MATRIZ DE INVENTARIO

inventario = [
    ["A001", "Papel resma 500 hojas",  20,  50],
    ["A002", "Bolígrafos azules",       80,  60],
    ["A003", "Carpetas manila",          5,  30],
    ["A004", "Marcadores permanentes",  12,  25],
    ["A005", "Clips metálicos x100",    45,  45],
    ["A006", "Tijeras medianas",         2,  15],
    ["A007", "Cuadernos cuadriculados", 70,  40],
]

# ***
# MÓDULO / FUNCIÓN: calcular_pedido

def calcular_pedido(stock_actual, stock_minimo):
    """
    Determina la cantidad a pedir para un artículo.

    Parámetros:
        stock_actual  (int): unidades disponibles actualmente.
        stock_minimo  (int): nivel mínimo requerido en bodega.

    Retorna:
        int: cantidad de unidades a solicitar (0 si no se necesita).
    """
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

# ***
# PROGRAMA PRINCIPAL
# ***
def main():
    print("=" * 55)
    print("       SISTEMA DE AUDITORÍA DE INVENTARIO")
    print("=" * 55)
    print(f"{'ARTÍCULO':<30} {'ACTUAL':>7} {'MÍNIMO':>7} {'PEDIR':>7}")
    print("-" * 55)

    pedidos = []   # lista para acumular artículos que necesitan reabastecimiento

    # Recorrer cada fila de la matriz
    for articulo in inventario:
        codigo       = articulo[0]
        nombre       = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        # Llamar al módulo para obtener la cantidad a pedir
        cantidad = calcular_pedido(stock_actual, stock_minimo)

        # Mostrar estado de cada artículo
        estado = "✔ OK" if cantidad == 0 else f"⚠  {cantidad} uds."
        print(f"{nombre:<30} {stock_actual:>7} {stock_minimo:>7}   {estado}")

        # Si se necesita pedir, agregar a la lista de pedidos
        if cantidad > 0:
            pedidos.append((nombre, cantidad))

    # ***
    # SALIDA: Lista de pedidos
    # ***
    print("=" * 55)
    print("           LISTA DE PEDIDOS A REALIZAR")
    print("=" * 55)

    if pedidos:
        for nombre, cantidad in pedidos:
            print(f"  Artículo: {nombre}")
            print(f"  → Pedir : {cantidad} unidades")
            print()
    else:
        print("  Todos los artículos tienen stock suficiente.")
        print("  No se requieren pedidos en este momento.")

    print("=" * 55)
    print(f"  Total de artículos auditados : {len(inventario)}")
    print(f"  Artículos que necesitan pedido: {len(pedidos)}")
    print("=" * 55)

# Punto de entrada del programa
if __name__ == "__main__":
    main()