def eliminar_duplicados(facturas):
    facturas_unicas = []

    for factura in facturas:
        factura = factura.strip().upper()

        if factura not in facturas_unicas:
            facturas_unicas.append(factura)

    return facturas_unicas

"""
ANALISIS:
Sintoma -> Reportes de ventas inconsistentes.  
Causa -> No existen reglas de unicidad y falta de formato en el número de facturas.
"""