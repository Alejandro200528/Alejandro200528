class perosna:
    def __init__(self, nombre, edad, nacionalidad):
        self.__nombre = nombre
        self.__edad = edad
        self.nacionalidad = nacionalidad

def get_nombre(self):
        return self.__nombre

class cliente(perosna):
    def __init__(self, nombre, edad, nacionalidad, compra , descuento ):
        super().__init__(nombre, edad, nacionalidad)
        self.compra = compra
        self.descuento = descuento

    def compra(self)
         return self._compra
    
    def get_descuento(self):
         return self.get_descuento
    
    def set_descuento(self,nuevo_descuento):
         sef ._descuento = nuevo_descuento


cliente1=cliente("libia",34,"argentina",200,0.1)
print(f"el nombre del  cliente es:{cliente1.get_nombre()}")
cliente1.set_descuento(0.2)
print(f"el nombre del cliente es:{cliente.get_descuento()}")


