def clave_segura(clave):
    if len(clave) < 8:
        return False

    tiene_mayuscula = any(letra.isupper() for letra in clave)
    tiene_minuscula = any(letra.islower() for letra in clave)
    tiene_numero = any(letra.isdigit() for letra in clave)

    return tiene_mayuscula and tiene_minuscula and tiene_numero

"""
ANALISIS:
Sintoma -> Contraseñas inseguras.
Causa -> El sistema no valida las contraseñas que se crean.
"""