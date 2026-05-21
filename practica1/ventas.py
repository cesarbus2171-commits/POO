class ventas:
    def __init__(self, idVenta, idauto, idCliente, precioVenta, fechaCompra, intere):
        self.idVenta = idVenta
        self.idauto = idauto
        self.idCliente = idCliente
        self.precioVenta = precioVenta
        self.fechaCompra = fechaCompra
        self.interes = intere

    def ganacia(self):
        ganancia = self.precioVenta * 0.1
        print(f"La ganancia de la venta {self.idVenta} es de ${ganancia}.")
        
venta1 = ventas(1, 1, 1, 20000, "2023-01-01", 5)
venta2 = ventas(2, 2, 2, 22000, "2023-02-01", 5)
venta3 = ventas(3, 3, 3, 18000, "2023-03-01", 5)

print(venta1.idVenta, venta1.idauto, venta1.idCliente, venta1.precioVenta, venta1.fechaCompra, venta1.interes)
print(venta2.idVenta, venta2.idauto, venta2.idCliente, venta2.precioVenta, venta2.fechaCompra, venta2.interes)
print(venta3.idVenta, venta3.idauto, venta3.idCliente, venta3.precioVenta, venta3.fechaCompra, venta3.interes)

venta1.ganacia()
venta2.ganacia()
venta3.ganacia()
        
