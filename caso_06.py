from datetime import datetime

def minutos_tarde(hora_entrada, hora_llegada, tolerancia=5):
    formato = "%H:%M"

    entrada = datetime.strptime(hora_entrada, formato)
    llegada = datetime.strptime(hora_llegada, formato)

    retraso = int((llegada - entrada).total_seconds() / 60)

    if retraso <= tolerancia:
        return 0

    return retraso

"""
ANALISIS:
Sintoma -> Reportes de ventas inconsistentes.  
Causa -> No existen reglas de unicidad y falta de formato en el número de facturas.
"""