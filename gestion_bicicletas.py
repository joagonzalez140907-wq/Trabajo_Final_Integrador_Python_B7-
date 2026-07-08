# Funciones para gestionar las bicicletas: registrar, listar,
# buscar y mostrar las que estan disponibles.

from bicicleta import Bicicleta
import persistencia
import utilidades


def buscar_bicicleta_por_codigo(lista_bicicletas, codigo):
    # Recorre la lista y devuelve la bicicleta con ese codigo.
    # Si no la encuentra devuelve None.
    for bicicleta in lista_bicicletas:
        if bicicleta.get_codigo() == codigo:
            return bicicleta
    return None


def registrar_bicicleta(lista_bicicletas):
    print("\n--- REGISTRAR BICICLETA ---")
    codigo = utilidades.pedir_texto_no_vacio("Ingrese el codigo (ejemplo B001): ")

    # Controlamos que el codigo no este ya registrado
    bicicleta_encontrada = buscar_bicicleta_por_codigo(lista_bicicletas, codigo)
    if bicicleta_encontrada is not None:
        print("Ya existe una bicicleta con ese codigo.")
        return

    print("Tipos posibles: comun / montaña / electrica")
    tipo = utilidades.pedir_texto_no_vacio("Ingrese el tipo: ")
    tarifa = utilidades.pedir_numero_entero_positivo("Ingrese la tarifa por hora ($): ")

    # Una bicicleta nueva siempre arranca disponible
    nueva_bicicleta = Bicicleta(codigo, tipo, tarifa, True)
    lista_bicicletas.append(nueva_bicicleta)
    persistencia.guardar_bicicletas(lista_bicicletas)
    print("Bicicleta registrada correctamente.")


def listar_bicicletas(lista_bicicletas):
    print("\n--- LISTA DE TODAS LAS BICICLETAS ---")
    if len(lista_bicicletas) == 0:
        print("No hay bicicletas registradas.")
        return

    for bicicleta in lista_bicicletas:
        bicicleta.mostrar_datos()


def listar_bicicletas_disponibles(lista_bicicletas):
    print("\n--- BICICLETAS DISPONIBLES ---")
    cantidad_disponibles = 0

    for bicicleta in lista_bicicletas:
        if bicicleta.get_disponible():
            bicicleta.mostrar_datos()
            cantidad_disponibles = cantidad_disponibles + 1

    if cantidad_disponibles == 0:
        print("En este momento no hay bicicletas disponibles.")
    else:
        print("Total de bicicletas disponibles:", cantidad_disponibles)
