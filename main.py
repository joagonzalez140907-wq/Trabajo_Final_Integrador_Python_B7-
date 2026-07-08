# =============================================================
#  Trabajo Final Integrador - Laboratorio de Python
#  Escenario 11: Sistema de alquiler de bicicletas
# =============================================================
#  Este es el programa principal. Muestra un menu y, segun la
#  opcion que elija el usuario, llama a la funcion correspondiente.

import os

import persistencia
import utilidades
import gestion_clientes
import gestion_bicicletas
import gestion_alquileres
import estadisticas


def mostrar_menu():
    print("\n==========================================")
    print("     SISTEMA DE ALQUILER DE BICICLETAS")
    print("==========================================")
    print("1  - Registrar cliente")
    print("2  - Listar clientes")
    print("3  - Modificar cliente")
    print("4  - Registrar bicicleta")
    print("5  - Listar todas las bicicletas")
    print("6  - Listar bicicletas disponibles")
    print("7  - Iniciar alquiler")
    print("8  - Finalizar alquiler (devolucion)")
    print("9  - Listar alquileres")
    print("10 - Listar alquileres en curso")
    print("11 - Ver estadisticas de utilizacion")
    print("0  - Salir")


def main():
    # Si no existe la carpeta datos la creamos.
    if not os.path.exists("datos"):
        os.mkdir("datos")

    # Al iniciar cargamos los datos guardados en los archivos JSON.
    lista_clientes = persistencia.cargar_clientes()
    lista_bicicletas = persistencia.cargar_bicicletas()
    lista_alquileres = persistencia.cargar_alquileres()

    print("Datos cargados:",
          len(lista_clientes), "clientes,",
          len(lista_bicicletas), "bicicletas,",
          len(lista_alquileres), "alquileres.")

    opcion = ""
    while opcion != "0":
        mostrar_menu()
        opcion = input("Elija una opcion: ").strip()

        if opcion == "1":
            gestion_clientes.registrar_cliente(lista_clientes)
            utilidades.pausar()
        elif opcion == "2":
            gestion_clientes.listar_clientes(lista_clientes)
            utilidades.pausar()
        elif opcion == "3":
            gestion_clientes.modificar_cliente(lista_clientes)
            utilidades.pausar()
        elif opcion == "4":
            gestion_bicicletas.registrar_bicicleta(lista_bicicletas)
            utilidades.pausar()
        elif opcion == "5":
            gestion_bicicletas.listar_bicicletas(lista_bicicletas)
            utilidades.pausar()
        elif opcion == "6":
            gestion_bicicletas.listar_bicicletas_disponibles(lista_bicicletas)
            utilidades.pausar()
        elif opcion == "7":
            gestion_alquileres.iniciar_alquiler(lista_clientes, lista_bicicletas, lista_alquileres)
            utilidades.pausar()
        elif opcion == "8":
            gestion_alquileres.finalizar_alquiler(lista_bicicletas, lista_alquileres)
            utilidades.pausar()
        elif opcion == "9":
            gestion_alquileres.listar_alquileres(lista_alquileres)
            utilidades.pausar()
        elif opcion == "10":
            gestion_alquileres.listar_alquileres_en_curso(lista_alquileres)
            utilidades.pausar()
        elif opcion == "11":
            estadisticas.mostrar_estadisticas(lista_clientes, lista_bicicletas, lista_alquileres)
            utilidades.pausar()
        elif opcion == "0":
            print("Gracias por usar el sistema. Hasta luego.")
        else:
            print("Opcion invalida. Intente de nuevo.")


# Aca empieza a ejecutarse el programa.
main()
