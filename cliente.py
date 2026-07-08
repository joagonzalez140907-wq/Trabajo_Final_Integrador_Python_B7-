# Clase que representa a un cliente del sistema de alquiler.
# Usamos atributos privados (empiezan con __) y accedemos a ellos
# con getters y setters, como se ve en Programacion Orientada a Objetos.

class Cliente:

    def __init__(self, dni, nombre, apellido, telefono):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono

    # ------- Getters -------
    def get_dni(self):
        return self.__dni

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_telefono(self):
        return self.__telefono

    # ------- Setters -------
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def set_telefono(self, telefono):
        self.__telefono = telefono

    # ------- Metodos -------
    def nombre_completo(self):
        return self.__nombre + " " + self.__apellido

    def mostrar_datos(self):
        print("DNI:", self.__dni)
        print("Nombre y apellido:", self.nombre_completo())
        print("Telefono:", self.__telefono)

    # Convierte el objeto en un diccionario para poder guardarlo en JSON.
    def convertir_a_diccionario(self):
        diccionario = {}
        diccionario["dni"] = self.__dni
        diccionario["nombre"] = self.__nombre
        diccionario["apellido"] = self.__apellido
        diccionario["telefono"] = self.__telefono
        return diccionario
