# tienda, inventario, producto, comprador

class Producto():
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def verPrecio(self):
        print(self.precio)
    
    def verNombre(self):
        print(self.nombre)

    
class Inventario():
    def __init__(self):
        self.inventario = []
    
    def agregarProducto(self, producto:Producto):
        self.inventario.append(producto)
        print(f"{producto.nombre} ha sido agregado")

    def eliminarProducto(self, producto:Producto):
        self.inventario.remove(producto)
        print(f"{producto.nombre} ha sido eliminado")

    def listarProductos(self):
        for producto in self.inventario:
            print(f"{producto.nombre}: ${producto.precio}")
    

class Tienda():
    def __init__(self, nombre, inventario:Inventario):
        self.nombre = nombre
        self.inventario = inventario.inventario
    
    def verInventario(self):
        print("Los productos son: \n")
        for producto in self.inventario:
            print(f"Producto: {producto.nombre}, precio: {producto.precio}")
        if len(self.inventario) == 0:
            print("Inventario vacio")
        print(f"El inventario cuenta con {len(self.inventario)} productos")

    def venderProducto(self, producto:Producto):
        if producto in self.inventario:
            self.inventario.remove(producto)
            print(f"{producto.nombre} vendido")
        else:
            print(f"{producto.nombre} ya fue vendido")


class Cliente():
    def __init__(self, nombre, tienda:Tienda):
        self.nombre = nombre
        self.productos_comprados = []
        self.tienda = tienda
    
    def comprarProducto(self, producto:Producto):
        if producto in self.tienda.inventario:
            self.tienda.venderProducto(producto)
    
    def verProductos(self):
        self.tienda.verInventario()
    


#Creando productos
television = Producto("Samsung", 20000)
laptop = Producto("Acer", 23000)
libro = Producto("Harry Potter", 500)
switch = Producto("Nintendo Switch", 7600)
audifonos = Producto("JBL", 789)

#Creando un almacen 
almacen = Inventario()

#Agregando productos al almacen
almacen.agregarProducto(television)
almacen.agregarProducto(laptop)
almacen.agregarProducto(libro)
almacen.agregarProducto(switch)
almacen.agregarProducto(audifonos)

#Listando todos los productos del almacen
almacen.listarProductos()

#Creando un nuevo negocio
negocio = Tienda("Negocio", almacen)

#Creando un nuevo cliente
usuario = Cliente("Luis", negocio)

#Comprando un producto
usuario.comprarProducto(television)

#Listando todos los productos del almacen 
negocio.verInventario()