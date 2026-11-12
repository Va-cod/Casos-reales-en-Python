def validar_cliente(nombre, correo, celular):
    errores = []

    if not isinstance(nombre, str) or not nombre.strip():
        errores.append("nombre vacío")

    if not isinstance(correo, str) or "@" not in correo or "." not in correo[correo.find("@") + 1:]:
        errores.append("correo inválido")

    celular_str = str(celular) if celular is not None else ""
    if not (len(celular_str) == 10 and celular_str.isdigit() and celular_str.startswith("3")):
        errores.append("celular inválido")

    return errores


"""
ANALISIS:
Sintoma -> Correos invalidos y mensajes que no llegan a los clientes.
Causa -> Ausencia de validaciones de formato y obligatoriedad en los datos ingresados.
"""
