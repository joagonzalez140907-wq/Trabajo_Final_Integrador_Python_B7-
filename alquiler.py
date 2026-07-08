class Alquiler:

    def __init__(self, numero, dni_cliente, codigo_bicicleta,
                 fecha_hora_inicio, fecha_hora_fin, importe, finalizado):
        self.__numero = numero
        self.__dni_cliente = dni_cliente
        self.__codigo_bicicleta = codigo_bicicleta
        self.__fecha_hora_inicio = fecha_hora_inicio
        self.__fecha_hora_fin = fecha_hora_fin   
        self.__importe = importe                  
        self.__finalizado = finalizado            

    
    def get_numero(self):
        return self.__numero

    def get_dni_cliente(self):
        return self.__dni_cliente

    def get_codigo_bicicleta(self):
        return self.__codigo_bicicleta

    def get_fecha_hora_inicio(self):
        return self.__fecha_hora_inicio

    def get_fecha_hora_fin(self):
        return self.__fecha_hora_fin

    def get_importe(self):
        return self.__importe

    def get_finalizado(self):
        return self.__finalizado


    def set_fecha_hora_fin(self, fecha_hora_fin):
        self.__fecha_hora_fin = fecha_hora_fin

    def set_importe(self, importe):
        self.__importe = importe

    def set_finalizado(self, finalizado):
        self.__finalizado = finalizado

    def mostrar_datos(self):
        print("Alquiler numero:", self.__numero)
        print("  DNI del cliente:", self.__dni_cliente)
        print("  Codigo de la bicicleta:", self.__codigo_bicicleta)
        print("  Inicio:", self.__fecha_hora_inicio)
        if self.__finalizado:
            print("  Fin:", self.__fecha_hora_fin)
            print("  Importe cobrado: $", self.__importe)
        else:
            print("  Estado: EN CURSO")


    def convertir_a_diccionario(self):
        diccionario = {}
        diccionario["numero"] = self.__numero
        diccionario["dni_cliente"] = self.__dni_cliente
        diccionario["codigo_bicicleta"] = self.__codigo_bicicleta
        diccionario["fecha_hora_inicio"] = self.__fecha_hora_inicio
        diccionario["fecha_hora_fin"] = self.__fecha_hora_fin
        diccionario["importe"] = self.__importe
        diccionario["finalizado"] = self.__finalizado
        return diccionario
