class persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def presentarse(self):
        return f"soy {self.nombre},tengo{self.edad}años y soy de {self.nacionalidad}"
    
class artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return f"mi habilidad es {self.habilidad}"
    
class escritor(persona,artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, libro):
        persona.__init__(nombre, edad, nacionalidad,)
        artista.__init__(self, habilidad)
        self.libro = libro
    def escribir_novelas(self):
        return f"Escribo en el libro {self.libro}"
    

                     