class Libro():
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestamo(self):
        if self.disponible:
            self.disponible = False
            print(f"{self.titulo} ha sido prestado")
        else:
            print(f"{self.titulo} no esta disponible")
    
    def regresar_libro(self):
        self.disponible = True
        print(f"{self.titulo} ha sido devuelto")


class Usuario():
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre    
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        if libro.disponible:
            libro.prestamo()
            self.libros_prestados.append(libro)
        else:
            print(f"{libro.titulo} no esta disponible")
    
    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.regresar_libro()
            self.libros_prestados.remove(libro)
        else:
            print(f"{libro.titulo} no lo has pedido prestado")
        
    
class Biblioteca():
    def __init__(self):
        self.libros = []
        self.usuarios = []
    
    def nuevo_libro(self, libro):
        self.libros.append(libro)
        print(f"{libro.titulo} ha sido agregado")

    def nuevo_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"{usuario.nombre} ha sido registrado")
        
    def libros_disponibles(self):
        print("Libros disponibles")
        for libro in self.libros:
            if libro.disponible:
                print(f"{libro.titulo} por {libro.autor}")


#Crear libros
libro1 = Libro("El resplandor", "Stephen King")
libro2 = Libro("1984", "George Orwell")


#Crear usuario
usuario1 = Usuario("Carlos", "001")

#Crear Biblioteca
libreria = Biblioteca()
libreria.nuevo_libro(libro1)
libreria.nuevo_libro(libro2)
libreria.nuevo_usuario(usuario1)

#Mostrar libros disponbles
libreria.libros_disponibles()

#Realizar prestamo
usuario1.prestar_libro(libro1)

#Mostrar libros despues de haber pedido prestado uno
libreria.libros_disponibles()

#Devolver libro
usuario1.devolver_libro(libro1)

#Mostrar libro despues de haber devuelto uno
libreria.libros_disponibles()