# Clases: Agencia ,Carro, Usuario
# #Se puede hacer compra y venta de vehículos
# #El usuario puede ver cuales están disponibles, el precio del auto y comprar uno

#Este es un ejercicio de POO en el cual crearemos la clase Agencia, Carro y Usuario
#El Usuario puede ver cuales estan disponibles, el precio del auto y comprar uno

class Carro():
    def __init__(self, nombre, marca, precio):
        self.nombre = nombre
        self.marca = marca
        self.precio = int(precio)
        self.disponibilidad = True

class Agencia():
    def __init__(self):
        self.carros_disponibles = []

    def nuevoCarro(self, carro):
        self.carros_disponibles.append(carro)


class Comprador():
    def __init__(self):
        self.carros_comprados = []
        
    def carros_disponibles(self, agencia):
        print("Los autos disponibles son: \n")
        for carro in agencia.carros_disponibles:
            precio = "{:,}".format(carro.precio)
            print(f"El precio de {carro.nombre} es ==> ${precio}")
        print("\n")
    
    def comprar_auto(self,carro,agencia):
        for c in agencia.carros_disponibles:
            if c == carro and c.disponibilidad:
                c.disponibilidad = False
                agencia.carros_disponibles.remove(c)
                print(f"{carro.nombre} vendido")


#Creando carros
corolla = Carro("Corolla", "Toyota", 123000)
camaro = Carro("Camaro", "Chevrolet", 400000)
suburban = Carro("Suburban", "Chevrolet", 500000)
mustang = Carro("Mustang", "Ford", 350000)

#Creando agencia
agencia = Agencia()

#Agregando carros a la agencia
agencia.nuevoCarro(corolla)
agencia.nuevoCarro(camaro)
agencia.nuevoCarro(suburban)
agencia.nuevoCarro(mustang)

#Creando un nuevo usuario
usuario = Comprador()

#Listando los carros disponibles
usuario.carros_disponibles(agencia)

#Comprando autos
usuario.comprar_auto(corolla,agencia)
usuario.comprar_auto(camaro, agencia)

#Listando los autos disponibles despues de comprar dos autos
usuario.carros_disponibles(agencia)