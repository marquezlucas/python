#Modulo 3 
#Objetos - Básico 

#ejercicio 1 - Mascota

class Mascota:
    def __init__ (self, nombre, raza, edad):
            self.nombre = nombre
            self.raza = raza
            self.edad = edad
    
    def saludar(self):
          print(f"{self.nombre} es un {self.raza} y tiene {self.edad} años")

mascota1= Mascota("Pepe","Labrador","tres")

print(f"{mascota1.nombre} es un {mascota1.raza} y  tiene {mascota1.edad} años")