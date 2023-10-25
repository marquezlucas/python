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


#ejercicio 2 - Persona

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir_datos(self):
        print(f'{self.nombre}, {self.edad}')

    def mayor_edad (self):
        if self.edad >= 18:
            self.imprimir_datos() 
            print('Es mayor de edad')
            return True
        else:
            self.imprimir_datos()
            print('Es menor de edad')
            return False
        
persona1 = Persona("Pedro", 15)
persona2 = Persona("Ana", 30)

personas = [persona1,persona2]
persona1.imprimir_datos()
persona1.mayor_edad()
persona2.mayor_edad()

#ejercicio 3 - Calculadora

class Calculadora:
    def __init__(self,valor1,valor2):
        self.valor1 = int(valor1)
        self.valor2 = int(valor2)

    def suma(self):
        suma = self.valor1 + self.valor2
        print(suma)
    def resta(self):
        resta = self.valor1 - self.valor2
        print(resta)
         
    def multiplicacion(self):
        multiplicacion = self.valor1 * self.valor2
        print(multiplicacion)
         
    def division(self):
        try:
            division = self.valor1 / self.valor2
            print(division)
        except: 
            ZeroDivisionError
            print('No se puede dividir por cero, pruebe con otro número')
        
       