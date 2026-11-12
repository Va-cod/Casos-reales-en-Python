def prioridad_ticket(impacto, urgencia):
    puntajes = {
        "alto": 3,
        "medio": 2,
        "bajo": 1
    }

    impacto = impacto.lower()
    urgencia = urgencia.lower()

    if impacto not in puntajes or urgencia not in puntajes:
        raise ValueError("El impacto y la urgencia deben ser alto, medio o bajo")

    total = puntajes[impacto] + puntajes[urgencia]

    if total == 6:
        return "P1"
    elif total == 5:
        return "P2"
    elif total == 4:
        return "P3"
    else:
        return "P4"

"""
ANALISIS:
Sintoma -> Fallas en el modulo que genera demoras para cambiar de solicitud.
Causa -> No hay una clasificación adecuada segun el impacto y urgencia.
"""