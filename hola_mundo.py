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

#4.
persona = ['Lucas','Márquez',38787487,1994,'Ciudad de Buenos Aires',0]
print(persona)

#5.
clave_personal = persona[2]*persona[3]
persona[5] = clave_personal
print(clave_personal)
print(persona)

#6.
receta = ['1.En el amasado hay que unir la harina y la sal con el agua con levadura disuelta.','3.Pre-hornear la masa para pizza','4.Es mejor usar tomate fresco','2.Hay que agregar el aceite de a poco']
receta.sort()
print(receta)
receta.sort(reverse=True)
print(receta)

#6) Tuplas
#1.
tupla1 = (1,2,3)
tupla2 = (4,5,6)
suma = [0,0,0]
producto = [0,0,0]
suma[0] = tupla1[0]+tupla2[0]
suma[1] = tupla1[1]+tupla2[1]
suma[2] = tupla1[2]+tupla2[2]
producto[0] = tupla1[0]*tupla2[0]
producto[1] = tupla1[1]*tupla2[1]
producto[2] = tupla1[2]*tupla2[2]
tupla3 = (suma,producto)
print(tupla3)

#2.
pgp_casera = (clave_personal,'LuCaS1511-')

#3.
#no se van a poder modificar porque las tuplas son inmutables

valoresFijos = (0.25,0.5,0.75)

valoresVariables = [100,100,100]
print(valoresVariables)

valoresVariables[0] = valoresVariables[0] * valoresFijos[0]
valoresVariables[1] = valoresVariables[1] * valoresFijos[1]
valoresVariables[2] = valoresVariables[2] * valoresFijos[2]
print(valoresVariables)

#7) Diccionarios
#1.
ingredientes = {'tomate':5,'cebolla':1,'ajo':2,'morron':1,'zanahoria':1,'puerro':2,'papa':3,'lentejas':'400gr','ternera':'400gr','salame':1}

#2.
print(persona)


usuario = {'nombre':persona[0],'apellido':persona[1],'DNI':[2],'anio_de_nacimiento':persona[3],'lugar_de_nacimiento':persona[4],'clave':persona[5]}
print(usuario)

#me confundi en el elemento 2 que seria la clave DNI asi que tuve que modificarlo
usuario['DNI']=38787487
print(usuario)

#3.
usuario['pgp_casera']=tupla3