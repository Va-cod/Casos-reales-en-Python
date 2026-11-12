import math

def cobro_parqueadero(minutos, tipo):
    tipo = tipo.lower()

    tarifas = {
        "carro": 3000,
        "moto": 1500
    }

    topes = {
        "carro": 25000,
        "moto": 12000
    }

    if tipo not in tarifas:
        raise ValueError("El tipo debe ser 'carro' o 'moto'")

    if minutos <= 15:
        return 0

    horas = math.ceil(minutos / 60)
    cobro = horas * tarifas[tipo]

    return min(cobro, topes[tipo])

"""
ANALISIS:
Sintoma -> Reclamos por cobros incoherentes.
Causa -> El cálculo de la tarifa no está estandarizada.
"""