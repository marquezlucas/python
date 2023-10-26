#Modulo 3 
#1)Objetos - Básico 

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
        
calculo1 = Calculadora(10,2.3)   
calculo2 = Calculadora(4,0)
calculo1.suma() 
calculo1.resta()   
calculo1.multiplicacion()
calculo1.division()
calculo2.division()


#ejercicio 4 - Agenda

class Agenda:
    def __init__(self):
        self.contactos = []

    def mostrar_menu(self):
        print("\nMenú:")
        print("a. Añadir contacto")
        print("b. Lista de contactos")
        print("c. Buscar contacto")
        print("d. Editar contacto")
        print("e. Cerrar agenda")

    def agregar_contacto(self,nombre,telefono,email):
        nuevo_contacto = {"nombre":nombre,"telefono":telefono,"email":email}
        self.contactos.append(nuevo_contacto)
    
    def mostrar_contactos(self):
        for i in self.contactos:
            print(f'Nombre: {i["nombre"]}, Telefóno: {i["telefono"]}, Email: {i["email"]}')

    def buscar_contacto(self,nombre):
        for contacto in self.contactos:
            if contacto['nombre']== nombre:
                print(f'El nombre es: {contacto["nombre"]}, con telefóno: {contacto["telefono"]}, email: {contacto["email"]}')
                return
        print(f"No se encontró un contacto con el nombre {nombre}")

    def editar_contacto(self,nombre):
        for contacto in self.contactos:
            if contacto ['nombre']==nombre:
                print("¿Qué queres editar?")
                print("1.Nombre")
                print("2.Telefóno")
                print("3.Email")
                opcion = input("Ingrese el número de una de las opciones: ")

                if opcion == '1':
                    nuevo_nombre = input("Ingrese el nuevo nombre: ")
                    contacto['nombre'] = nuevo_nombre
                    print("Nombre actualizado.")
                elif opcion == '2':
                    nuevo_telefono = input("Ingrese el nuevo teléfono: ")
                    contacto['telefono'] = nuevo_telefono
                    print("Teléfono actualizado.")
                elif opcion == '3':
                    nuevo_email = input("Ingrese el nuevo email: ")
                    contacto['email'] = nuevo_email
                    print("Email actualizado.")
                else:
                    print("Opción no válida.")
                return
        print(f"No se encontró un contacto con el nombre {nombre}")
agenda = Agenda()

while True:
    agenda.mostrar_menu()
    opcion = input("Ingrese la opción deseada (a/b/c/d/e): ")

    if opcion == 'a':
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        email = input("Ingrese el email del contacto: ")
        agenda.agregar_contacto(nombre, telefono, email)
    elif opcion == 'b':
        agenda.mostrar_contactos()
    elif opcion == 'c':
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        agenda.buscar_contacto(nombre)
    elif opcion == 'd':
        nombre = input("Ingrese el nombre del contacto a editar: ")
        agenda.editar_contacto(nombre)
    elif opcion == 'e':
        break
    else:
        print("Opción no válida. Por favor, ingrese a, b, c, d o e.")

#2)Objetos - Clases anidadas 
#2.1

class Alumno:
    def __init__(self,nombre,apellido,edad,DNI,materias):
        self.nombre = str(nombre)
        self.apellido = str(apellido)
        self.edad = int(edad)
        self.DNI = int(DNI)
        self.materias = materias

#2.2 creo un metodo para tener el promedio anual

    def obtener_promedio_anio(self, anio):
        promedio_anual = [materia['nota'] for materia in self.materias['anio']== anio]
        if promedio_anual:
            return sum(promedio_anual) / len(promedio_anual)
        else:
            return 0
        
#creo un metodo para tener el promedio anual
    def obtener_promedio_general (self):
        notas = [materia['nota']for materia in self.materias]
        if notas:
            return sum(notas) / len(notas)
        else:
            return 0

#creo metodo para tener la mejor materia
    def mejor_materia(self):
        if self.materias:
            mejor_materia = max(self.materias, key = lambda materia: materia['nota'])
            return mejor_materia['nombre']
        else:
            return 'No hay materias registradas'

class Materias:
    def __init__(self,nombre,anio,nota):
        self.nombre = nombre
        self.anio = anio
        self.nota = nota