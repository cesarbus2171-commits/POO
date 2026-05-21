class proveedor:
    def __init__(self, idProv, nombre, empresa, direccion, producto, puesto):
        self.idProv = idProv
        self.nombre = nombre
        self.empresa = empresa
        self.direccion = direccion
        self.producto = producto
        self.puesto = puesto

    def pedido(self):
        print(f"El proveedor {self.nombre} ha realizado un pedido de {self.producto}.")

auto1 = proveedor(1, "Juan Pérez", "AutoSAC", "Calle 123", "Ruedas", "Vendedor")
auto2 = proveedor(2, "María García", "AutoSAC", "Avenida 456", "Motor", "Gerente")
auto3 = proveedor(3, "Carlos López", "AutoSAC", "Boulevard 789", "Frenos", "Supervisor")

print(auto1.idProv, auto1.nombre, auto1.empresa, auto1.direccion, auto1.producto, auto1.puesto)
print(auto2.idProv, auto2.nombre, auto2.empresa, auto2.direccion, auto2.producto, auto2.puesto)
print(auto3.idProv, auto3.nombre, auto3.empresa, auto3.direccion, auto3.producto, auto3.puesto)

auto1.pedido()
auto2.pedido()
auto3.pedido()