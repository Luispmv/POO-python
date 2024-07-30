#Ejemplo de Herencia en POO

#Clase padre
class Vehiculo():
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.disponible = True

    def vender(self):
        if self.disponible:
            self.disponible = False
            print(f"{self.marca} ha sido vendido")
        else:
            print(f"El vehiculo {self.marca}. No esta disponible")

    def revisar_disponibilidad(self):
        return self.disponible
    
    def obtener_precio(self):
        return self.precio
    
    def iniciar_motor(self):
        raise NotImplementedError("Este metodo deber ser implementado por la subclase")
    
    def detener_motor(self):
        raise NotImplementedError("Este metodo deber ser implementado por la subclase")
    

#Subclases    

class Auto(Vehiculo):

    def iniciar_motor(self):
        if not self.disponible:
            return f"{self.brand} Auto en marcha"
        else:
            return f"{self.brand} Auto no esta disponible"
    
    def detener_motor(self):
        if self.disponible:
            return f"{self.brand} Auto se ha detendido"
        else:
            return f"{self.brand} Auto no esta disponible"


class Bike(Vehiculo):
    def iniciar_motor(self):
        if not self.disponible:
            return f"{self.brand} bici en marcha"
        else:
            return f"{self.brand} bici no disponible"
    
    def detener_motor(self):
        if self.disponible:
            return f"{self.brand} bici se ha detendido"
        else:
            return f"{self.brand} bici no disponible"
        

class Camion(Vehiculo):
    def iniciar_motor(self):
        if not self.disponible:
            return f"{self.brand} camion en marcha"
        else:
            return f"{self.brand} camion no disponible"
    
    def detener_motor(self):
        if self.disponible:
            return f"{self.brand} camion se ha detendido"
        else:
            return f"{self.brand} camion no disponible"
        

class Comprador():
    def __init__(self, nombre):
        self.nombre = nombre
        self.autos_comprados = []
    
    def comprar_vehiculo(self, vehiculo: Vehiculo):
        if vehiculo.revisar_disponibilidad():
            vehiculo.vender()
            self.autos_comprados.append(vehiculo)
        else:
            print(f"Los siento {vehiculo.marca} no disponible")
    
    def ver_vehiculo(self, vehiculo: Vehiculo):
        if vehiculo.revisar_disponibilidad():
            disponibilidad = "Disponible"
        else:
            disponibilidad = "No Disponible"
        print(f"El {vehiculo.marca} esta {disponibilidad} y cuesta {vehiculo.obtener_precio()}")


class agencia():
    def __init__(self):
        self.inventario = []
        self.clientes = []
    
    def añadirVehiculo(self, vehiculo:Vehiculo):
        self.inventario.append(vehiculo)
        print(f"El {vehiculo.marca} ha sido añadido al inventario")
    
    def añadirCliente(self, cliente:Comprador):
        self.clientes.append(cliente)
        print(f"{cliente.nombre} ha sido añadido")
    
    def listarVehiculos(self):
        print("Vehiculos disponibles:")
        for vehiculo in self.inventario:
            if vehiculo.revisar_disponibilidad():
                print(f"{vehiculo.marca} ==> {vehiculo.obtener_precio()}")


#Creando vehiculos
car = Auto("Toyota", "Corolla", 200000)
bicicleta = Bike("Yamaha", "MT-07", 7000)
camion = Camion("Volvo", "FH16", 800000)

#Creando cliente
cliente = Comprador("Manuel")

#Creando agencia 
tienda = agencia()

# Añadiendo vehiculos a la tienda
tienda.añadirVehiculo(car)
tienda.añadirVehiculo(bicicleta)
tienda.añadirVehiculo(camion)

#Listamos todos los vehiculos de la tienda
tienda.listarVehiculos()

#Vemos los vehiculos disponibles
cliente.ver_vehiculo(car)

#Compramos un carro
cliente.comprar_vehiculo(car)

#Listamos los vehiculos despues de comprar uno
tienda.listarVehiculos()


