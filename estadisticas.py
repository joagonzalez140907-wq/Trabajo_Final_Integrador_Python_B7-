from gestion_clientes import buscar_cliente_por_dni
from gestion_alquileres import calcular_minutos_de_uso


def calcular_recaudacion_total(lista_alquileres):
   
    total = 0
    for alquiler in lista_alquileres:
        if alquiler.get_finalizado():
            total = total + alquiler.get_importe()
    return total


def calcular_minutos_totales(lista_alquileres):
   
    total_minutos = 0
    for alquiler in lista_alquileres:
        if alquiler.get_finalizado():
            minutos = calcular_minutos_de_uso(alquiler.get_fecha_hora_inicio(),
                                              alquiler.get_fecha_hora_fin())
            total_minutos = total_minutos + minutos
    return total_minutos


def contar_alquileres_por_bicicleta(lista_alquileres):
  
    contador = {}
    for alquiler in lista_alquileres:
        codigo = alquiler.get_codigo_bicicleta()
        if codigo in contador:
            contador[codigo] = contador[codigo] + 1
        else:
            contador[codigo] = 1
    return contador


def contar_alquileres_por_cliente(lista_alquileres):
   
    contador = {}
    for alquiler in lista_alquileres:
        dni = alquiler.get_dni_cliente()
        if dni in contador:
            contador[dni] = contador[dni] + 1
        else:
            contador[dni] = 1
    return contador


def buscar_clave_con_mayor_valor(diccionario):
    
    clave_ganadora = ""
    valor_mas_alto = 0
    for clave in diccionario:
        if diccionario[clave] > valor_mas_alto:
            valor_mas_alto = diccionario[clave]
            clave_ganadora = clave
    return clave_ganadora


def mostrar_estadisticas(lista_clientes, lista_bicicletas, lista_alquileres):
    print("\n--- ESTADISTICAS DE UTILIZACION ---")

    if len(lista_alquileres) == 0:
        print("Todavia no hay alquileres registrados.")
        return


    print("Clientes registrados:", len(lista_clientes))
    print("Bicicletas registradas:", len(lista_bicicletas))
    print("Total de alquileres:", len(lista_alquileres))

  
    recaudacion = calcular_recaudacion_total(lista_alquileres)
    print("Recaudacion total: $", recaudacion)


    minutos_totales = calcular_minutos_totales(lista_alquileres)
    print("Tiempo total de uso:", minutos_totales, "minutos.")


    contador_bicicletas = contar_alquileres_por_bicicleta(lista_alquileres)
    codigo_mas_alquilada = buscar_clave_con_mayor_valor(contador_bicicletas)
    cantidad = contador_bicicletas[codigo_mas_alquilada]
    print("Bicicleta mas alquilada:", codigo_mas_alquilada,
          "con", cantidad, "alquileres.")


    contador_clientes = contar_alquileres_por_cliente(lista_alquileres)
    dni_mejor_cliente = buscar_clave_con_mayor_valor(contador_clientes)
    cantidad = contador_clientes[dni_mejor_cliente]
    cliente = buscar_cliente_por_dni(lista_clientes, dni_mejor_cliente)
    if cliente is not None:
        nombre_cliente = cliente.nombre_completo()
    else:
        nombre_cliente = "DNI " + dni_mejor_cliente
    print("Cliente con mas alquileres:", nombre_cliente,
          "con", cantidad, "alquileres.")
