from datetime import datetime

from alquiler import Alquiler
import persistencia
import utilidades
from gestion_clientes import buscar_cliente_por_dni
from gestion_bicicletas import buscar_bicicleta_por_codigo


FORMATO_FECHA = "%d/%m/%Y %H:%M"


def obtener_fecha_hora_actual():
  
    ahora = datetime.now()
    return ahora.strftime(FORMATO_FECHA)


def calcular_minutos_de_uso(fecha_inicio_texto, fecha_fin_texto):
    
    fecha_inicio = datetime.strptime(fecha_inicio_texto, FORMATO_FECHA)
    fecha_fin = datetime.strptime(fecha_fin_texto, FORMATO_FECHA)
    diferencia = fecha_fin - fecha_inicio
    total_segundos = diferencia.total_seconds()
    minutos = int(total_segundos / 60)
    return minutos


def calcular_importe(minutos_de_uso, tarifa_por_hora):
    
    horas_a_cobrar = minutos_de_uso // 60
    if minutos_de_uso % 60 != 0:
        horas_a_cobrar = horas_a_cobrar + 1
    if horas_a_cobrar < 1:
        horas_a_cobrar = 1
    importe = horas_a_cobrar * tarifa_por_hora
    return importe


def obtener_proximo_numero(lista_alquileres):
  
    numero_mas_grande = 0
    for alquiler in lista_alquileres:
        if alquiler.get_numero() > numero_mas_grande:
            numero_mas_grande = alquiler.get_numero()
    return numero_mas_grande + 1


def buscar_alquiler_en_curso_de_bicicleta(lista_alquileres, codigo_bicicleta):
  
    for alquiler in lista_alquileres:
        if alquiler.get_codigo_bicicleta() == codigo_bicicleta:
            if not alquiler.get_finalizado():
                return alquiler
    return None


def iniciar_alquiler(lista_clientes, lista_bicicletas, lista_alquileres):
    print("\n--- INICIAR ALQUILER ---")

    dni = utilidades.pedir_texto_no_vacio("Ingrese el DNI del cliente: ")
    cliente = buscar_cliente_por_dni(lista_clientes, dni)
    if cliente is None:
        print("No existe un cliente con ese DNI. Primero debe registrarlo.")
        return

    codigo = utilidades.pedir_texto_no_vacio("Ingrese el codigo de la bicicleta: ")
    bicicleta = buscar_bicicleta_por_codigo(lista_bicicletas, codigo)
    if bicicleta is None:
        print("No existe una bicicleta con ese codigo.")
        return

    if not bicicleta.get_disponible():
        print("Esa bicicleta ya esta alquilada.")
        return

    
    numero = obtener_proximo_numero(lista_alquileres)
    fecha_hora_inicio = obtener_fecha_hora_actual()
    nuevo_alquiler = Alquiler(numero, dni, codigo, fecha_hora_inicio, "", 0, False)
    lista_alquileres.append(nuevo_alquiler)

    
    bicicleta.set_disponible(False)

    persistencia.guardar_alquileres(lista_alquileres)
    persistencia.guardar_bicicletas(lista_bicicletas)

    print("Alquiler numero", numero, "iniciado.")
    print("Cliente:", cliente.nombre_completo())
    print("Fecha y hora de inicio:", fecha_hora_inicio)


def finalizar_alquiler(lista_bicicletas, lista_alquileres):
    print("\n--- FINALIZAR ALQUILER (DEVOLUCION) ---")

    codigo = utilidades.pedir_texto_no_vacio("Ingrese el codigo de la bicicleta que se devuelve: ")
    alquiler = buscar_alquiler_en_curso_de_bicicleta(lista_alquileres, codigo)
    if alquiler is None:
        print("No hay ningun alquiler en curso para esa bicicleta.")
        return

    bicicleta = buscar_bicicleta_por_codigo(lista_bicicletas, codigo)

    
    fecha_hora_fin = obtener_fecha_hora_actual()
    minutos_de_uso = calcular_minutos_de_uso(alquiler.get_fecha_hora_inicio(), fecha_hora_fin)
    importe = calcular_importe(minutos_de_uso, bicicleta.get_tarifa_por_hora())

    
    alquiler.set_fecha_hora_fin(fecha_hora_fin)
    alquiler.set_importe(importe)
    alquiler.set_finalizado(True)

    
    bicicleta.set_disponible(True)

    persistencia.guardar_alquileres(lista_alquileres)
    persistencia.guardar_bicicletas(lista_bicicletas)

    print("Alquiler numero", alquiler.get_numero(), "finalizado.")
    print("Tiempo de uso:", minutos_de_uso, "minutos.")
    print("Importe a cobrar: $", importe)


def listar_alquileres(lista_alquileres):
    print("\n--- LISTA DE ALQUILERES ---")
    if len(lista_alquileres) == 0:
        print("No hay alquileres registrados.")
        return

    for alquiler in lista_alquileres:
        alquiler.mostrar_datos()
        print("------------------------------")


def listar_alquileres_en_curso(lista_alquileres):
    print("\n--- ALQUILERES EN CURSO ---")
    cantidad_en_curso = 0

    for alquiler in lista_alquileres:
        if not alquiler.get_finalizado():
            alquiler.mostrar_datos()
            print("------------------------------")
            cantidad_en_curso = cantidad_en_curso + 1

    if cantidad_en_curso == 0:
        print("No hay alquileres en curso.")
