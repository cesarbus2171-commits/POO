class clientes:
    def __init__(self, idCliente, nombre, apellido, sexo, correo, direccion):
        self.idCliente = idCliente
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.correo = correo
        self.direccion = direccion

    def aprobacion(self):
        print(f"El cliente {self.nombre} {self.apellido} ha sido aprobado.")
    
cliente1 = clientes(1, "Ana", "García", "Femenino", "ana.garcia@email.com", "Calle 123")
cliente2 = clientes(2, "Luis", "Martínez", "Masculino", "luis.martinez@email.com", "Avenida 456")
cliente3 = clientes(3, "María", "Rodríguez", "Femenino", "maria.rodriguez@email.com", "Boulevard 789")

print(cliente1.idCliente, cliente1.nombre, cliente1.apellido, cliente1.sexo, cliente1.correo, cliente1.direccion)
print(cliente2.idCliente, cliente2.nombre, cliente2.apellido, cliente2.sexo, cliente2.correo, cliente2.direccion)
print(cliente3.idCliente, cliente3.nombre, cliente3.apellido, cliente3.sexo, cliente3.correo, cliente3.direccion)

cliente1.aprobacion()
cliente2.aprobacion()
cliente3.aprobacion()
