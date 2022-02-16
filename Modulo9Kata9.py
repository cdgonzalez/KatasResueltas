### Ejercicio: Uso de funciones en Python
### Ejercicio 1: Trabajar con argumentos en funciones

def reporte_combustible(main_tank, external_tank, reserve_tank):
    return f"""Reporte de Combustible en la nave:
    Total : {promedio([main_tank, external_tank, reserve_tank])}%
    Tanque Principal: {main_tank}%
    Exterior: {external_tank}%
    Tanque de Reserva: {reserve_tank}% 
    """

def promedio(values):
    total = sum(values)
    tanques = len(values)
    return (total / tanques)

print(reporte_combustible(50,60,80))


### Ejercicio 2: Trabajo con argumentos de palabra clave
### Ejercicio : Trabajar con argumentos de palabras clave en funciones

def informe_mision(prelanzamiento, tiempo_vuelo, destino, tanque_externo, tanque_interno):
    return f"""
    Misión con destino a: {destino}
    Tiempo total de viaje: {prelanzamiento + tiempo_vuelo} minutos
    Combustible restante: {tanque_externo + tanque_interno} gallones
    """

print(informe_mision(14, 51, "Luna", 200000, 300000))

## actualización de las funciones *minutes y **fuel_reservoirs:
def informe_mision(destino, *minutos, **reserva_combustible):
    return f"""
    Misión a: {destino}
    Tiempo total de viaje: {sum(minutos)} minutos
    Combustible restante total: {sum(reserva_combustible.values())}
    """

print(informe_mision("Luna", 10, 15, 51, Principal=300000, Externo=200000)) 

### Actualización nombre para cada tanque
def informe_mision(destino, *minutos, **reserva_combustible):
    reporte = f"""
    Misión a: {destino}
    Tiempo total de viaje: {sum(minutos)} minutos
    Combustible restante total: {sum(reserva_combustible.values())}
    """
    for nombre_tanque, gallones in reserva_combustible.items():
        reporte += f"Tanque {nombre_tanque}: --> {gallones} gallones restantes\n"
    return reporte

print(informe_mision("Luna", 8, 11, 55, Principal=300000, Externo=200000))