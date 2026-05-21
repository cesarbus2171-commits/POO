class empleados:
    def __init__(self, idEmpleado, nombre, apellido, sexo, curp, puesto, salario):
        self.idEmpleado = idEmpleado
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.curp = curp
        self.puesto = puesto
        self.salario = salario

    def nomina(self):
        print(f"Nomina del empleado {self.nombre} {self.apellido}: ${self.salario}")

empleado1 = empleados(1, "Juan", "Perez", "M", "CURP1", "Desarrollador", 50000)
empleado2 = empleados(2, "Maria", "Garcia", "F", "CURP2", "Diseñadora", 45000)
empleado3 = empleados(3, "Carlos", "Lopez", "M", "CURP3", "Gerente", 60000)

print(empleado1.idEmpleado, empleado1.nombre, empleado1.apellido, empleado1.sexo, empleado1.curp, empleado1.puesto, empleado1.salario)
print(empleado2.idEmpleado, empleado2.nombre, empleado2.apellido, empleado2.sexo, empleado2.curp, empleado2.puesto, empleado2.salario)
print(empleado3.idEmpleado, empleado3.nombre, empleado3.apellido, empleado3.sexo, empleado3.curp, empleado3.puesto, empleado3.salario)

empleado1.nomina()
empleado2.nomina()
empleado3.nomina()