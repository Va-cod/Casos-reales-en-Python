def vehiculos_necesarios(pesos, capacidad):
    """Calcula cuántos vehículos se necesitan para transportar los paquetes."""

    if not pesos:
        return 0

    camiones = 1
    carga_actual = 0

    for peso in pesos:

        if peso > capacidad:
            return -1

        if carga_actual + peso <= capacidad:
            carga_actual += peso
        else:
            camiones += 1
            carga_actual = peso

    return camiones


"""
ANALISIS:
Sintoma -> Dias con camiones de mas o dias con paquetes pendientes por despachar.
Causa -> Falta de un sistema de optimización que determine la cantidad óptima de vehículos necesarios para transportar los paquetes.
"""