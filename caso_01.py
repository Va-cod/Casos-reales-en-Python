
def clasificar_cartera(dias_mora):
    if dias_mora <= 0:
        return "Al día"
    elif dias_mora <= 30:
        return "1-30 días"
    elif dias_mora <= 60:
        return "31-60 días"
    elif dias_mora <= 90:
        return "61-90 días"
    elif dias_mora >= 91:
        return "Más de 90 días"

clasificar_cartera(0)

"""
ANALISIS:
Sintoma -> Facturas con días de mora en aumento y algunas son dificiles de recuperar.
Causa -> No exite un criterio o clasificación adecuada de las facturas para determinar que llamadas se deben realizar de primero.
"""
