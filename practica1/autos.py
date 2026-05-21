class autos:
    def __init__(self, idauto, modelo, version, color, precio, mantenimiento):
        self.idauto = idauto
        self.modelo = modelo
        self.version = version
        self.color = color
        self.precio = precio
        self.mantenimiento = mantenimiento

    def venta(self):
        print(f"El auto {self.modelo} {self.version} de color {self.color} se ha vendido por ${self.precio}.")

auto1 = autos(1, "Toyota", "Corolla", "Rojo", 20000, "Anual")
auto2 = autos(2, "Honda", "Civic", "Azul", 22000, "Semestral")
auto3 = autos(3, "Ford", "Focus", "Negro", 18000, "Anual")

print(auto1.modelo, auto1.version, auto1.color, auto1.precio, auto1.mantenimiento)
print(auto2.modelo, auto2.version, auto2.color, auto2.precio, auto2.mantenimiento)
print(auto3.modelo, auto3.version, auto3.color, auto3.precio, auto3.mantenimiento)

auto1.venta()
auto2.venta()
auto3.venta()