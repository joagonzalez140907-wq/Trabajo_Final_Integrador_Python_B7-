def pedir_texto_no_vacio(mensaje):
    
    texto = input(mensaje)
    texto = texto.strip()
    while texto == "":
        print("El dato no puede quedar vacio. Intente de nuevo.")
        texto = input(mensaje)
        texto = texto.strip()
    return texto


def pedir_numero_entero_positivo(mensaje):
    
    while True:
        texto = input(mensaje)
        texto = texto.strip()
        if texto.isdigit():
            numero = int(texto)
            if numero > 0:
                return numero
        print("Debe ingresar un numero entero mayor a cero.")


def pausar():
    
    input("\nPresione Enter para continuar...")
