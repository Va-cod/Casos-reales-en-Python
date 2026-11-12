def pago_horas_extra(valor_hora, diurnas, nocturnas):
    total = ((valor_hora * diurnas)*1.25) + ((valor_hora * nocturnas)*1.75)
    return round(total)

"""
ANALISIS:
Sintoma -> Pago de horas extra que no coinciden con las cuentas reales y reprocesos.
Causa -> Los calculos de pago se realiza de manera manual.
"""
