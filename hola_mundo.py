entrada = input("Ingrese un nombre: ")
print("Hola "+ entrada)

ls = [1,2,3,4,5]

ls[0] =15

ls

ls[1:5:2]

ls = [1,2,3,4,5,6]

###python.nivelinicial@gmail.com

# Practica 1
#2)
# 1.

num = 131

#2.

palabra = 'asdasd'

#3.

v1 = 5
v2 = 8
v3 = 'Lucas'

#3)
#1.

#a) 8
a = 2+3+1+2
print(a)
#b) 7
b = 2+3*1+2
print(b)
#c) 7
c = (2+3)*1+2
print(c)
#d) 15
d = (2+3)*(1+2)
print(d)
#e)-6
e = +---6
print(e)
#f) +6
f = -+-+6
print(f)

#4) Strings
#1.

cadena = 'Estoy aprendiendo Python'
print(cadena)

#2.
párrafo = """
En Python es posible
armar un párrafo
muy sencillamente
"""
print(párrafo)

#3. 
hoy = cadena[0:-6]
print(hoy)

#4.
complejo = (párrafo[3:13], párrafo[-14:-1], párrafo[-18:-15], párrafo[14:21])
print(complejo[0],complejo[1],complejo[2],complejo[3])


#5)  Listas
#1.
numeros = [1,2,3,4,5]
print(numeros[2])

#2.
colores =  ["rojo","verde","azul"]
colores[1] = 'amarillo'
print(colores)

#3.
frutas = ["manzana","naranja","uva"]
frutas += ['banana']
frutas.remove('naranja')
print(frutas)



#6) Tuplas
#1.
valoresFijos = (0.25,0.5,0.75)

valoresVariables = [100,100,100]
print(valoresVariables)

valoresVariables[0] = valoresVariables[0] * valoresFijos[0]
valoresVariables[1] = valoresVariables[1] * valoresFijos[1]
valoresVariables[2] = valoresVariables[2] * valoresFijos[2]
print(valoresVariables)

#7) Diccionarios