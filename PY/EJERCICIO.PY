
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Empleado(Persona):
    def __init__(self, nombre, edad, salario, area):
        super().__init__(nombre, edad)
        self.salario = salario
        self.area = area

class Vendedor(Empleado):
    def __init__(self, nombre, edad, salario, area, venta, sucursal):
        super().__init__(nombre, edad, salario, area)
        self.venta = venta
        self.sucursal = sucursal

    def calcular_comision(self):
        return self.venta * 0.11

    def calcular_venta_descuento(self):
        return self.venta * 0.9


class Cliente(Persona):
    def __init__(self, nombre, edad, compra, bono):
        super().__init__(nombre, edad)
        self.compra = compra
        self.bono = bono


vendedor = Vendedor("Juan", 30, 25000, "Ventas", 10000, "Sucursal B")
comision = vendedor.calcular_comision()
venta_con_descuento = vendedor.calcular_venta_descuento()

print(f"Comisión del vendedor: {comision} €")
print(f"Venta con descuento: {venta_con_descuento} €")




