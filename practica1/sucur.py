class sucursal:
    def __init__(self, idSucursal, idAuto, cantidad, fechaIngreso, disponibilidad):
        self.idSucursal = idSucursal
        self.idAuto = idAuto
        self.cantidad = cantidad
        self.fechaIngreso = fechaIngreso
        self.disponibilidad = disponibilidad

    def ingresar(self):
        print(f"El auto con id {self.idAuto} ha sido ingresado a la sucursal con id {self.idSucursal}.")

sucursal1 = sucursal(1, 1, 10, "2023-09-01", True)
sucursal2 = sucursal(2, 2, 5, "2023-09-15", True)
sucursal3 = sucursal(3, 3, 8, "2023-10-01", True)

print(sucursal1.idSucursal, sucursal1.idAuto, sucursal1.cantidad, sucursal1.fechaIngreso, sucursal1.disponibilidad)
print(sucursal2.idSucursal, sucursal2.idAuto, sucursal2.cantidad, sucursal2.fechaIngreso, sucursal2.disponibilidad)
print(sucursal3.idSucursal, sucursal3.idAuto, sucursal3.cantidad, sucursal3.fechaIngreso, sucursal3.disponibilidad)

sucursal1.ingresar()
sucursal2.ingresar()
sucursal3.ingresar()