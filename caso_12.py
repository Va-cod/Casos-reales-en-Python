def pendientes_conciliar(banco, contabilidad):
    """Devuelve los valores del banco que no tienen pareja en contabilidad."""

    pendientes = []
    contabilidad_disponible = contabilidad.copy()

    for valor in banco:
        if valor in contabilidad_disponible:
            contabilidad_disponible.remove(valor)
        else:
            pendientes.append(valor)

    return pendientes

"""
ANALISIS:
Sintoma -> Diferencias entre los registros del banco y la contabilidad.
Causa -> Falta de un sistema de conciliación efectivo para identificar y resolver las discrepancias entre los dos conjuntos de datos.
"""