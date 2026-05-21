class prueba:
    def __init__(self, idPrueba, idSucursal, idEmpleado, idCliente, fecha):
        self.idPrueba = idPrueba
        self.idSucursal = idSucursal
        self.idEmpleado = idEmpleado
        self.idCliente = idCliente
        self.fecha = fecha

    def reagendar(self):
        self.fecha = input("Ingrese la nueva fecha para la prueba: ")
        print("Reagendando prueba con id: ", self.idPrueba)

cliente1 = prueba(1, 1, 1, 1, "2023-10-10")
cliente2 = prueba(2, 1, 2, 2, "2023-11-15")
cliente3 = prueba(3, 2, 3, 3, "2023-12-20")

print(cliente1.idPrueba, cliente1.idSucursal, cliente1.idEmpleado, cliente1.idCliente, cliente1.fecha)
print(cliente2.idPrueba, cliente2.idSucursal, cliente2.idEmpleado, cliente2.idCliente, cliente2.fecha)
print(cliente3.idPrueba, cliente3.idSucursal, cliente3.idEmpleado, cliente3.idCliente, cliente3.fecha)

cliente1.reagendar()
cliente2.reagendar()
cliente3.reagendar()