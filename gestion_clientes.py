# Funciones para gestionar los clientes: registrar, listar, buscar y modificar.

from cliente import Cliente
import persistencia
import utilidades


def buscar_cliente_por_dni(lista_clientes, dni):
    # Recorre la lista y devuelve el cliente con ese DNI.
    # Si no lo encuentra devuelve None.
    for cliente in lista_clientes:
        if cliente.get_dni() == dni:
            return cliente
    return None


def registrar_cliente(lista_clientes):
    print("\n--- REGISTRAR CLIENTE ---")
    dni = utilidades.pedir_texto_no_vacio("Ingrese el DNI: ")

    # Controlamos que el DNI no este ya registrado
    cliente_encontrado = buscar_cliente_por_dni(lista_clientes, dni)
    if cliente_encontrado is not None:
        print("Ya existe un cliente con ese DNI.")
        return

    nombre = utilidades.pedir_texto_no_vacio("Ingrese el nombre: ")
    apellido = utilidades.pedir_texto_no_vacio("Ingrese el apellido: ")
    telefono = utilidades.pedir_texto_no_vacio("Ingrese el telefono: ")

    nuevo_cliente = Cliente(dni, nombre, apellido, telefono)
    lista_clientes.append(nuevo_cliente)
    persistencia.guardar_clientes(lista_clientes)
    print("Cliente registrado correctamente.")


def listar_clientes(lista_clientes):
    print("\n--- LISTA DE CLIENTES ---")
    if len(lista_clientes) == 0:
        print("No hay clientes registrados.")
        return

    for cliente in lista_clientes:
        cliente.mostrar_datos()
        print("------------------------------")


def modificar_cliente(lista_clientes):
    print("\n--- MODIFICAR CLIENTE ---")
    dni = utilidades.pedir_texto_no_vacio("Ingrese el DNI del cliente a modificar: ")

    cliente = buscar_cliente_por_dni(lista_clientes, dni)
    if cliente is None:
        print("No se encontro un cliente con ese DNI.")
        return

    print("Datos actuales del cliente:")
    cliente.mostrar_datos()

    nuevo_nombre = utilidades.pedir_texto_no_vacio("Ingrese el nuevo nombre: ")
    nuevo_apellido = utilidades.pedir_texto_no_vacio("Ingrese el nuevo apellido: ")
    nuevo_telefono = utilidades.pedir_texto_no_vacio("Ingrese el nuevo telefono: ")

    cliente.set_nombre(nuevo_nombre)
    cliente.set_apellido(nuevo_apellido)
    cliente.set_telefono(nuevo_telefono)

    persistencia.guardar_clientes(lista_clientes)
    print("Cliente modificado correctamente.")
