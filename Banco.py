class CuentaBancaria():
    def __init__(self, propietario, balance):
        self.propietario = propietario
        self.balance = balance
        self.activa = True
    
    def desactivar_cuenta(self):
        self.activa = False
        print("Cuenta inactiva :(")
    
    def activar_cuenta(self):
        self.activa = True
        print("Cuenta activa :)")
    
    def depositar(self, cantidad):
        if self.activa:
            self.balance += cantidad
            print(f"Se ha depositado {cantidad}. Saldo Actual {self.balance}")
        else:
            self.desactivar_cuenta()
    
    def retirar(self, cantidad):
        if self.activa:
            if cantidad <= self.balance:
                self.balance -= cantidad
                print(f"Se ha retirado {cantidad}. Saldo Actual {self.balance}")
            else:
                print("Cantidad insuficiente")
        else:
            self.desactivar_cuenta()

cuenta1 = CuentaBancaria("Mariano", 234)
cuenta1.depositar(1500)
cuenta1.retirar(300)
cuenta1.desactivar_cuenta()
cuenta1.depositar(200)
cuenta1.activar_cuenta()
cuenta1.depositar(2000)



