def cantidad_a_pedir(stock, demanda_diaria, dias_entrega, stock_seguridad, stock_max):
    """Calcula la cantidad de unidades que se deben pedir."""

    punto_reorden = (demanda_diaria * dias_entrega) + stock_seguridad

    if stock <= punto_reorden:
        return stock_max - stock

    return 0

"""
ANALISIS:
Sintoma -> Productos agotados y clientes insatisfechos.
Causa -> Falta de un sistema de control de inventario que determine cuándo y cuánto pedir para mantener un stock adecuado.
"""