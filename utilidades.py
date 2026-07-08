# Funciones auxiliares para pedir datos por teclado.
# Las separamos en este archivo porque las usamos en varios lugares
# y asi no repetimos el mismo codigo.


def pedir_texto_no_vacio(mensaje):
    # Pide un texto y lo vuelve a pedir mientras este vacio.
    texto = input(mensaje)
    texto = texto.strip()
    while texto == "":
        print("El dato no puede quedar vacio. Intente de nuevo.")
        texto = input(mensaje)
        texto = texto.strip()
    return texto


def pedir_numero_entero_positivo(mensaje):
    # Pide un numero entero mayor a cero y lo vuelve a pedir si no es valido.
    while True:
        texto = input(mensaje)
        texto = texto.strip()
        if texto.isdigit():
            numero = int(texto)
            if numero > 0:
                return numero
        print("Debe ingresar un numero entero mayor a cero.")


def pausar():
    # Espera a que el usuario presione Enter para seguir.
    input("\nPresione Enter para continuar...")
