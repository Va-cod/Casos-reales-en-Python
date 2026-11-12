def lotes_para_retirar(lotes):
    """Devuelve los códigos de los lotes que deben retirarse."""
    return [
        codigo
        for codigo, dias in sorted(lotes, key=lambda lote: lote[1])
        if dias <= 7
    ]

"""
ANALISIS:
Sintoma -> Lotes que se vencen y no se retiran a tiempo.
Causa -> Falta de un sistema de seguimiento efectivo para identificar y retirar los lotes vencidos.
"""