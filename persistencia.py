# Este modulo se encarga de guardar y cargar los datos en archivos JSON.
# Asi los clientes, bicicletas y alquileres no se pierden al cerrar el programa.

import json
import os

from cliente import Cliente
from bicicleta import Bicicleta
from alquiler import Alquiler

# Nombres de los archivos donde guardamos cada cosa
ARCHIVO_CLIENTES = "datos/clientes.json"
ARCHIVO_BICICLETAS = "datos/bicicletas.json"
ARCHIVO_ALQUILERES = "datos/alquileres.json"


def guardar_lista_en_archivo(lista_de_objetos, nombre_archivo):
    # Convierte cada objeto en diccionario y guarda la lista en el JSON.
    lista_de_diccionarios = []
    for objeto in lista_de_objetos:
        lista_de_diccionarios.append(objeto.convertir_a_diccionario())

    archivo = open(nombre_archivo, "w", encoding="utf-8")
    json.dump(lista_de_diccionarios, archivo, indent=4, ensure_ascii=False)
    archivo.close()


def leer_lista_del_archivo(nombre_archivo):
    # Lee el JSON y devuelve la lista de diccionarios.
    # Si el archivo todavia no existe, devuelve una lista vacia.
    if not os.path.exists(nombre_archivo):
        return []

    archivo = open(nombre_archivo, "r", encoding="utf-8")
    lista_de_diccionarios = json.load(archivo)
    archivo.close()
    return lista_de_diccionarios


# ---------- Clientes ----------

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


# ---------- Bicicletas ----------

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


# ---------- Alquileres ----------

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
