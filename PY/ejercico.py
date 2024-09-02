class Persona:
    def _init_(self,nombre,edad,nacionalidad):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad 

class Empleado:
    def _init_(self, salario, sucursal):
        self.salario=salario
        self.sucursal=sucursal

class Planta(Persona, Empleado):
    def _init_(self, nombre, edad, nacionalidad, salario, sucursal, bono, saldo_h_extras,desc_seguridad):
        Persona._init_(self, nombre, edad, nacionalidad)
        Empleado._init_(self, salario, sucursal)
        self.bono=bono
        self.saldo_h_extras=saldo_h_extras
        self.desc_seguridad=desc_seguridad

    def sueldo_planta(self):
                  return self.salario + self.bono + self.saldo_h_extras - self.desc_seguridad 
        

class Contratista(Persona, Empleado):
    def _init_(self, nombre, edad, nacionalidad, salario, sucursal, retefuente):
        Persona._init_(self, nombre, edad, nacionalidad)
        Empleado._init_(self, salario, sucursal)
        self.retefuente=retefuente

    def sueldo_contratista(self):
         return self.salario - self.retefuente
        

planta1 = Planta('alverto',21,'colombia',2100000,'cartagena',300000,400000,100000)
contratista1 = Contratista('alejandro',18,'Colombiano',2300000,'santa marta',(2400000*0.03))

print(f'El salario final de planta es de {planta1.sueldo_planta()}')
print(f'El salario final de contratistra es de {contratista1.sueldo_contratista()}')