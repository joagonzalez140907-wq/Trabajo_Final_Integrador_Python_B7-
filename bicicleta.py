# Clase que representa una bicicleta del parque.
# Cada bicicleta tiene un codigo, un tipo, una tarifa por hora
# y un estado que indica si esta disponible para alquilar.

class Bicicleta:

    def __init__(self, codigo, tipo, tarifa_por_hora, disponible):
        self.__codigo = codigo
        self.__tipo = tipo  # por ejemplo: comun, montaña, electrica
        self.__tarifa_por_hora = tarifa_por_hora
        self.__disponible = disponible  # True si se puede alquilar

    # ------- Getters -------
    def get_codigo(self):
        return self.__codigo

    def get_tipo(self):
        return self.__tipo

    def get_tarifa_por_hora(self):
        return self.__tarifa_por_hora

    def get_disponible(self):
        return self.__disponible

    # ------- Setters -------
    def set_tipo(self, tipo):
        self.__tipo = tipo

    def set_tarifa_por_hora(self, tarifa_por_hora):
        self.__tarifa_por_hora = tarifa_por_hora

    def set_disponible(self, disponible):
        self.__disponible = disponible

    # ------- Metodos -------
    def mostrar_datos(self):
        # Segun el estado mostramos un texto u otro
        if self.__disponible:
            estado = "Disponible"
        else:
            estado = "Alquilada"
        print("Codigo:", self.__codigo,
              "| Tipo:", self.__tipo,
              "| Tarifa por hora: $", self.__tarifa_por_hora,
              "| Estado:", estado)

    # Convierte el objeto en un diccionario para poder guardarlo en JSON.
    def convertir_a_diccionario(self):
        diccionario = {}
        diccionario["codigo"] = self.__codigo
        diccionario["tipo"] = self.__tipo
        diccionario["tarifa_por_hora"] = self.__tarifa_por_hora
        diccionario["disponible"] = self.__disponible
        return diccionario
