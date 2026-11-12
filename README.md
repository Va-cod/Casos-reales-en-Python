# 💼 Taller de Lógica de Negocio y Automatización - SENA

Repositorio correspondiente al taller práctico de desarrollo de software del **SENA (Servicio Nacional de Aprendizaje)**. Contiene la resolución algorítmica de **12 situaciones reales de negocio** donde procesos manuales o empíricos causaban pérdidas de tiempo, dinero o inconsistencias operativas.

Cada caso incluye:
1. **Identificación de Síntoma y Causa Raíz** (Análisis del problema).
2. **Implementación de Solución Algorítmica en Python** con validaciones y reglas de negocio estandarizadas.

---

## 📋 Resumen de Casos y Soluciones

| # | Archivo | Función Principal | Área / Dominio | Regla de Negocio / Objetivo |
|:---:|:---|:---|:---|:---|
| **01** | [`caso_01.py`](caso_01.py) | `clasificar_cartera(dias_mora)` | Cartera y Cobranza | Priorización de cobro según rangos de mora (al día, 1-30, 31-60, 61-90, +90 días). |
| **02** | [`caso_02.py`](caso_02.py) | `pago_horas_extra(valor_hora, diurnas, nocturnas)` | Nómina y RRHH | Liquidación estandarizada de recargos (diurnas: +25%, nocturnas: +75%). |
| **03** | [`caso_03.py`](caso_03.py) | `clave_segura(clave)` | Seguridad TI | Política de contraseñas: mínimo 8 caracteres, con mayúscula, minúscula y número. |
| **04** | [`caso_04.py`](caso_04.py) | `prioridad_ticket(impacto, urgencia)` | Mesa de Ayuda (ITSM) | Matriz de priorización de incidentes (P1 a P4) según impacto y urgencia. |
| **05** | [`caso_05.py`](caso_05.py) | `eliminar_duplicados(facturas)` | Facturación | Limpieza y deduplicación insensible a espacios y mayúsculas/minúsculas. |
| **06** | [`caso_06.py`](caso_06.py) | `minutos_tarde(hora_entrada, hora_llegada, tolerancia=5)` | Control de Acceso | Cálculo de retardos con margen de tolerancia configurable. |
| **07** | [`caso_07.py`](caso_07.py) | `cobro_parqueadero(minutos, tipo)` | Operaciones / Comercial | Cobro por hora/fracción con 15 min de gracia y topes diarios (Carro/Moto). |
| **08** | [`caso_08.py`](caso_08.py) | `validar_cliente(nombre, correo, celular)` | CRM / Marketing | Validación de formulario de registro: no vacíos, formato email y celular de 10 dígitos. |
| **09** | [`caso_09.py`](caso_09.py) | `lotes_para_retirar(lotes)` | Calidad y Retail | Detección y ordenamiento prioritario de lotes críticos a vencer ($\le 7$ días). |
| **10** | [`caso_10.py`](caso_10.py) | `cantidad_a_pedir(...)` | Cadena de Suministro | Punto de reorden y cálculo automático de reabastecimiento para evitar desabastecimiento. |
| **11** | [`caso_11.py`](caso_11.py) | `vehiculos_necesarios(pesos, capacidad)` | Logística y Despacho | Empaquetamiento y cubicaje de carga para optimizar el alquiler de camiones. |
| **12** | [`caso_12.py`](caso_12.py) | `pendientes_conciliar(banco, contabilidad)` | Finanzas y Contabilidad | Conciliación bancaria automatizada uno a uno evitando falsos cruces por valores iguales. |

---

## 🔍 Detalle de Situaciones Empresariales

### 🔹 Situación 1: Gestión de Cartera
> **Contexto:** El área de cartera de una distribuidora llama a los clientes en el orden en que aparecen en el Excel. Mientras tanto, las facturas con más de 90 días de mora siguen creciendo y algunas ya son difíciles de recuperar.
- **Archivo:** [`caso_01.py`](caso_01.py)
- **Función:** `clasificar_cartera(dias_mora)`
- **Síntoma:** Facturas con días de mora en aumento y algunas son difíciles de recuperar.
- **Causa:** No existe un criterio o clasificación adecuada de las facturas para determinar qué llamadas realizar primero.

---

### 🔹 Situación 2: Liquidación de Horas Extra
> **Contexto:** Cada quincena los operarios reclaman porque el pago de horas extra no coincide con sus cuentas. El auxiliar de nómina las liquida a mano con calculadora, y cada mes alguien aplica un recargo distinto.
- **Archivo:** [`caso_02.py`](caso_02.py)
- **Función:** `pago_horas_extra(valor_hora, diurnas, nocturnas)`
- **Síntoma:** Pago de horas extra que no coinciden con las cuentas reales y reprocesos continuos.
- **Causa:** Los cálculos se realizan manualmente sin estandarización de recargos.

---

### 🔹 Situación 3: Seguridad en Contraseñas ERP
> **Contexto:** Una auditoría encontró usuarios del ERP con claves como «123456» y «empresa». Se pidió a todos cambiarlas, pero tres meses después hay de nuevo claves débiles.
- **Archivo:** [`caso_03.py`](caso_03.py)
- **Función:** `clave_segura(clave)`
- **Síntoma:** Contraseñas inseguras en sistemas corporativos.
- **Causa:** El sistema no valida las políticas de complejidad al momento de la creación o cambio.

---

### 🔹 Situación 4: Priorización de Incidentes en Mesa de Ayuda
> **Contexto:** La mesa de ayuda atiende los casos por orden de llegada. Un lunes, la caída del módulo de facturación esperó dos horas detrás de una solicitud para cambiar el fondo de pantalla.
- **Archivo:** [`caso_04.py`](caso_04.py)
- **Función:** `prioridad_ticket(impacto, urgencia)`
- **Síntoma:** Fallas críticas desatendidas mientras se atienden solicitudes operativas menores.
- **Causa:** Ausencia de una matriz de clasificación objetiva por impacto y urgencia (niveles P1 a P4).

---

### 🔹 Situación 5: Conciliación y Deduplicación de Ventas
> **Contexto:** El reporte de ventas del mes muestra más dinero del que llegó al banco. Después de dos días revisando, contabilidad descubre facturas repetidas: algunas idénticas y otras con espacios o en minúscula.
- **Archivo:** [`caso_05.py`](caso_05.py)
- **Función:** `eliminar_duplicados(facturas)`
- **Síntoma:** Reportes de ventas inflados que no coinciden con el dinero real recibido.
- **Causa:** Inexistencia de reglas de unicidad y falta de normalización de cadenas de texto (mayúsculas y espacios).

---

### 🔹 Situación 6: Registro Biométrico y Control de Puntualidad
> **Contexto:** Recursos humanos revisa a mano el reporte del reloj biométrico para descontar retardos. Hay reclamos porque a unos se les descontó llegar 3 minutos tarde y a otros no se les descontaron 20.
- **Archivo:** [`caso_06.py`](caso_06.py)
- **Función:** `minutos_tarde(hora_entrada, hora_llegada, tolerancia=5)`
- **Síntoma:** Reclamos e inequidades en los descuentos salariales por tardanza.
- **Causa:** Proceso manual y subjetivo sin una regla automatizada de tolerancia.

---

### 🔹 Situación 7: Tarifas y Cobro de Parqueadero
> **Contexto:** El parqueadero de un centro comercial cobra según el criterio de cada cajero. Algunos redondean la fracción de hora hacia abajo y otros hacia arriba, y los clientes reclaman por cobros diferentes por el mismo tiempo.
- **Archivo:** [`caso_07.py`](caso_07.py)
- **Función:** `cobro_parqueadero(minutos, tipo)`
- **Síntoma:** Reclamos por cobros incoherentes y diferencias tarifarias por el mismo tiempo de permanencia.
- **Causa:** Cálculo de tarifa no estandarizado. Regla aplicada: primeros 15 min gratis ($0), cobro por hora o fracción posterior (61 min = 2 horas) con tope diario de \$25.000 para carro y \$12.000 para moto.

---

### 🔹 Situación 8: Validación de Datos de Clientes
> **Contexto:** La última campaña de correo rebotó en cientos de envíos y muchos SMS no llegaron. Al revisar la base de clientes aparecen correos sin «@», celulares de 7 dígitos y registros sin nombre.
- **Archivo:** [`caso_08.py`](caso_08.py)
- **Función:** `validar_cliente(nombre, correo, celular)`
- **Síntoma:** Correos rebotados y mensajes SMS que no llegan a los clientes.
- **Causa:** Falta de validaciones obligatorias de formato al capturar la información del cliente.

---

### 🔹 Situación 9: Control de Vencimientos en Góndola
> **Contexto:** Un supermercado recibió una sanción porque se encontraron productos vencidos en góndola. Los auxiliares revisan fechas a ojo, pasillo por pasillo, y nunca alcanzan a terminar.
- **Archivo:** [`caso_09.py`](caso_09.py)
- **Función:** `lotes_para_retirar(lotes)`
- **Síntoma:** Sanciones y pérdidas por productos vencidos en estantería.
- **Causa:** Falta de un sistema automatizado de alertas que priorice lotes con 7 días o menos de vida útil.

---

### 🔹 Situación 10: Reabastecimiento de Inventario
> **Contexto:** Una ferretería se queda sin cemento cada mes. El jefe de compras pide cuando ve la estantería casi vacía, pero el proveedor tarda varios días en entregar y en ese tiempo se pierden ventas.
- **Archivo:** [`caso_10.py`](caso_10.py)
- **Función:** `cantidad_a_pedir(stock, demanda_diaria, dias_entrega, stock_seguridad, stock_max)`
- **Síntoma:** Productos agotados, pérdida de ventas y clientes insatisfechos.
- **Causa:** Compras intuitivas sin considerar el tiempo de entrega del proveedor ni el stock de seguridad (punto de reorden).

---

### 🔹 Situación 11: Cubicaje y Optimización de Camiones
> **Contexto:** Una empresa de mensajería alquila camiones cada mañana según el cálculo del coordinador. Unos días sobran camiones pagados y otros días quedan paquetes en bodega.
- **Archivo:** [`caso_11.py`](caso_11.py)
- **Función:** `vehiculos_necesarios(pesos, capacidad)`
- **Síntoma:** Días con exceso de camiones pagados o días con paquetes rezagados en bodega.
- **Causa:** Estimación empírica en vez de un cálculo sistemático basado en la capacidad de carga.

---

### 🔹 Situación 12: Conciliación Bancaria Automática
> **Contexto:** Contabilidad tarda tres días cada mes cruzando, línea por línea, el extracto bancario contra los registros contables. Cuando hay dos pagos del mismo valor, se confunden y hay que empezar de nuevo.
- **Archivo:** [`caso_12.py`](caso_12.py)
- **Función:** `pendientes_conciliar(banco, contabilidad)`
- **Síntoma:** Tiempos excesivos (tres días) y reprocesos constantes al conciliar partidas del mismo valor.
- **Causa:** Proceso manual vulnerable a duplicidades y emparejamientos erróneos.

---

## 🚀 Requisitos y Ejecución

### Requisitos
- **Python 3.8** o superior instalado.

### Ejecución de Pruebas Rápidas
Puedes importar y probar cualquier función desde el intérprete interactivo de Python:

```bash
# Iniciar la consola interactiva de Python en la raíz del proyecto
python
```

```python
# Ejemplo: Probar cobro de parqueadero (Caso 07)
from caso_07 import cobro_parqueadero
print(cobro_parqueadero(15, "carro"))   # 0 (primeros 15 min gratis)
print(cobro_parqueadero(61, "carro"))   # 6000 (2 horas)
print(cobro_parqueadero(600, "carro"))  # 25000 (tope alcanzado)

# Ejemplo: Validar cliente (Caso 08)
from caso_08 import validar_cliente
print(validar_cliente("Ana Perez", "ana@correo.com", "3001234567")) # []
print(validar_cliente("", "invalido", "123")) # ['nombre vacío', 'correo inválido', 'celular inválido']
```

---

## 🛠️ Tecnologías y Metodología
- **Lenguaje:** Python 3
- **Metodología:** Análisis de Causa Raíz (RCA - Root Cause Analysis) aplicado a problemas empresariales cotidianos.
- **Principios:** Funciones puras, código modular, control defensivo de tipos y manejo robusto de excepciones.
