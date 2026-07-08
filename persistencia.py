import json
import os

from cliente import Cliente
from bicicleta import Bicicleta
from alquiler import Alquiler


ARCHIVO_CLIENTES = "datos/clientes.json"
ARCHIVO_BICICLETAS = "datos/bicicletas.json"
ARCHIVO_ALQUILERES = "datos/alquileres.json"


def guardar_lista_en_archivo(lista_de_objetos, nombre_archivo):
   
    lista_de_diccionarios = []
    for objeto in lista_de_objetos:
        lista_de_diccionarios.append(objeto.convertir_a_diccionario())

    archivo = open(nombre_archivo, "w", encoding="utf-8")
    json.dump(lista_de_diccionarios, archivo, indent=4, ensure_ascii=False)
    archivo.close()


def leer_lista_del_archivo(nombre_archivo):
   
    if not os.path.exists(nombre_archivo):
        return []

    archivo = open(nombre_archivo, "r", encoding="utf-8")
    lista_de_diccionarios = json.load(archivo)
    archivo.close()
    return lista_de_diccionarios




def guardar_clientes(lista_clientes):
    guardar_lista_en_archivo(lista_clientes, ARCHIVO_CLIENTES)


def cargar_clientes():
    lista_clientes = []
    lista_de_diccionarios = leer_lista_del_archivo(ARCHIVO_CLIENTES)
    for diccionario in lista_de_diccionarios:
        cliente = Cliente(diccionario["dni"],
                          diccionario["nombre"],
                          diccionario["apellido"],
                          diccionario["telefono"])
        lista_clientes.append(cliente)
    return lista_clientes




def guardar_bicicletas(lista_bicicletas):
    guardar_lista_en_archivo(lista_bicicletas, ARCHIVO_BICICLETAS)


def cargar_bicicletas():
    lista_bicicletas = []
    lista_de_diccionarios = leer_lista_del_archivo(ARCHIVO_BICICLETAS)
    for diccionario in lista_de_diccionarios:
        bicicleta = Bicicleta(diccionario["codigo"],
                              diccionario["tipo"],
                              diccionario["tarifa_por_hora"],
                              diccionario["disponible"])
        lista_bicicletas.append(bicicleta)
    return lista_bicicletas




def guardar_alquileres(lista_alquileres):
    guardar_lista_en_archivo(lista_alquileres, ARCHIVO_ALQUILERES)


def cargar_alquileres():
    lista_alquileres = []
    lista_de_diccionarios = leer_lista_del_archivo(ARCHIVO_ALQUILERES)
    for diccionario in lista_de_diccionarios:
        alquiler = Alquiler(diccionario["numero"],
                            diccionario["dni_cliente"],
                            diccionario["codigo_bicicleta"],
                            diccionario["fecha_hora_inicio"],
                            diccionario["fecha_hora_fin"],
                            diccionario["importe"],
                            diccionario["finalizado"])
        lista_alquileres.append(alquiler)
    return lista_alquileres
