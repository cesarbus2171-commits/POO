class stock:
    def __init__(self, idStock, idAuto, cantidad, fechaIngreso, disponibilidad):
        self.idStock = idStock
        self.idAuto = idAuto
        self.cantidad = cantidad
        self.fechaIngreso = fechaIngreso
        self.disponibilidad = disponibilidad

    def eliminarStock(self):
        self.disponibilidad = False
        print(f"El stock con id {self.idStock} ha sido eliminado.")

stock1 = stock(1, 1, 10, "2023-09-01", True)
stock2 = stock(2, 2, 5, "2023-09-15", True)
stock3 = stock(3, 3, 8, "2023-10-01", True)

print(stock1.idStock, stock1.idAuto, stock1.cantidad, stock1.fechaIngreso, stock1.disponibilidad)
print(stock2.idStock, stock2.idAuto, stock2.cantidad, stock2.fechaIngreso, stock2.disponibilidad)
print(stock3.idStock, stock3.idAuto, stock3.cantidad, stock3.fechaIngreso, stock3.disponibilidad)

stock1.eliminarStock()
stock2.eliminarStock()
stock3.eliminarStock()