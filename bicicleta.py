class Bicicleta:

    def __init__(self, codigo, tipo, tarifa_por_hora, disponible):
        self.__codigo = codigo
        self.__tipo = tipo 
        self.__tarifa_por_hora = tarifa_por_hora
        self.__disponible = disponible 


    def get_codigo(self):
        return self.__codigo

    def get_tipo(self):
        return self.__tipo

    def get_tarifa_por_hora(self):
        return self.__tarifa_por_hora

    def get_disponible(self):
        return self.__disponible

   
    def set_tipo(self, tipo):
        self.__tipo = tipo

    def set_tarifa_por_hora(self, tarifa_por_hora):
        self.__tarifa_por_hora = tarifa_por_hora

    def set_disponible(self, disponible):
        self.__disponible = disponible

  
    def mostrar_datos(self):
     
        if self.__disponible:
            estado = "Disponible"
        else:
            estado = "Alquilada"
        print("Codigo:", self.__codigo,
              "| Tipo:", self.__tipo,
              "| Tarifa por hora: $", self.__tarifa_por_hora,
              "| Estado:", estado)


    def convertir_a_diccionario(self):
        diccionario = {}
        diccionario["codigo"] = self.__codigo
        diccionario["tipo"] = self.__tipo
        diccionario["tarifa_por_hora"] = self.__tarifa_por_hora
        diccionario["disponible"] = self.__disponible
        return diccionario
