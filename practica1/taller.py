class taller:
    def __init__(self, idTaller, idauto, idSucursal, idEmpleado, idCliente, fechaIngreso):
        self.idTaller = idTaller
        self.idauto = idauto
        self.idSucursal = idSucursal
        self.idEmpleado = idEmpleado
        self.idCliente = idCliente
        self.fechaIngreso = fechaIngreso

    def cita(self):
        print(f"El cliente {self.idCliente} ha solicitado una cita en el taller {self.idTaller}.")

auto1 = taller(1, 1, 1, 1, 1, "2023-01-01")
auto2 = taller(2, 2, 2, 2, 2, "2023-02-01")
auto3 = taller(3, 3, 3, 3, 3, "2023-03-01")

print(auto1.idTaller, auto1.idauto, auto1.idSucursal, auto1.idEmpleado, auto1.idCliente, auto1.fechaIngreso)
print(auto2.idTaller, auto2.idauto, auto2.idSucursal, auto2.idEmpleado, auto2.idCliente, auto2.fechaIngreso)
print(auto3.idTaller, auto3.idauto, auto3.idSucursal, auto3.idEmpleado, auto3.idCliente, auto3.fechaIngreso)

auto1.cita()
auto2.cita()
auto3.cita()