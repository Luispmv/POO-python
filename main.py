class Persona:
    #Constructor 
    #En el constructor name y age son los atrivutos de la clase 
    #self permite que cuando hagamos instancias de la clase, estas instancias tengan atributos name y age
    def __init__(self, name, age):
        self.name =  name
        self.age =  age
    
    #Metodos de la clase
    #Haciendo uno de los atributos de la clase, podemos manipular estos mediante metodos en nuestra clase
    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age}")

    

#Llamando a nuestra clase
person1 = Persona("Luis", 21)
person1.greet()

