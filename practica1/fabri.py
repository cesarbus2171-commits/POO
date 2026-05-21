class fabricacion:
    def __init__(self, idAutoFab, idauto, idProvedor, fechaFab,precioFab, progreso):
        self.idAutoFab = idAutoFab
        self.idauto = idauto
        self.idProvedor = idProvedor
        self.fechaFab = fechaFab
        self.precioFab = precioFab
        self.progreso = progreso

    def actualizar(self):
        self.progreso = "Completado"
        print(f"El auto {self.idauto} ha sido actualizado con el progreso: {self.progreso}")

auto1 = fabricacion(1, 1, 1, "2023-01-01", 20000, "En proceso")
auto2 = fabricacion(2, 2, 2, "2023-02-01", 22000, "En proceso")
auto3 = fabricacion(3, 3, 3, "2023-03-01", 18000, "En proceso")

print(auto1.idAutoFab, auto1.idauto, auto1.idProvedor, auto1.fechaFab, auto1.precioFab, auto1.progreso)
print(auto2.idAutoFab, auto2.idauto, auto2.idProvedor, auto2.fechaFab, auto2.precioFab, auto2.progreso)
print(auto3.idAutoFab, auto3.idauto, auto3.idProvedor, auto3.fechaFab, auto3.precioFab, auto3.progreso)

auto1.actualizar()
auto2.actualizar()
auto3.actualizar()