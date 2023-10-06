#Modulo 2 
#controladores de flujo 

#ejercicio 1

# Definimos una lista de números
numeros = [1,2,3,4,5,6,7,8,9,10] # La suma total de los números pares es 30

# Declaramos una variables para sumar los números pares.
sumaPares = 0

# Declarar una función que sume los números pares
def siEsParSuma(num, sum):
    if num % 2 == 0:
        sum += num
    return sum

# Recorrer la lista de números
for numero in numeros: # POR CADA numero EN numeros
    sumaPares = siEsParSuma(numero, sumaPares)

# Imprimimos en pantalla la suma total de números pares
print("La suma total de los pares de la lista es:", sumaPares)

#Entradas y salidas de datos
#calculadora facil

# Declaramos variables para solicitar datos desde la consola al usuario
primerNumero = float(input("Ingrese el primer número: "))
segundoNumero = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación matemática (+,-,*,/): ")

# Realizar las operaciones y mostrar el resultado
if operacion == '+':
    resultado = primerNumero + segundoNumero
elif operacion == '-':
    resultado = primerNumero - segundoNumero
elif operacion == '*':
    resultado = primerNumero * segundoNumero
elif operacion == '/':
    if segundoNumero != 0:
        resultado = primerNumero / segundoNumero
    else:
        print("Error: No se puede dividir por cero.")
else:
    print("Operación no valida")

# Imprimimos el resultado en pantalla
print(f'El resultado de {primerNumero} {operacion} {segundoNumero} es igual a {resultado}')

#calculadora dificil

# Vamos a crear una función para solicitar números al usuario
def solicitar_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, ingresa un número valido")

# Función para realizar las operaciones matematicas
def calcular(primerNumero, segundoNumero, operacion):
    if operacion == '+':
        return primerNumero + segundoNumero
    elif operacion == '-':
        return primerNumero - segundoNumero
    elif operacion == '*':
        return primerNumero * segundoNumero
    elif operacion == '/':
        if segundoNumero != 0:
            return primerNumero / segundoNumero
        else:
            return "Error: No se puede dividir por cero."
    else:
        return "Operación no valida"

# Función principal
def main():
    primerNumero = solicitar_numero("Ingrese el primer número: ")
    segundoNumero = solicitar_numero("Ingrese el segundo número: ")
    operacion = input("Ingrese la operación matemática (+,-,/,*): ")

    # Llamamos a la función para calcular los inputs
    resultado = calcular(primerNumero, segundoNumero, operacion)

    # Imprimimos en pantalla
    print(f'El resultado de {primerNumero} {operacion} {segundoNumero} es igual a {resultado}')

# Vamos a ejecutar nuestra función principal cuando ejecutemos el script
if __name__ == "__main__":
    main()

#division multiples resultados

# Vamos a crear una función llamada dividir
def dividir(dividendo, divisor):
    if divisor == 0:
        return 'No se puede dividir por cero.'
    else:
        resultado = dividendo / divisor
        resto = dividendo % divisor
        return resultado, resto

# Llamamos a la función con dos números
dividendo = float(input("Ingrese el dividendo: "))
divisor = float(input("Ingrese el divisor: "))
resultado, resto = dividir(dividendo, divisor)

# Mostramos los valores en pantalla
print(f'Resultado de la división: {resultado} y el resto es: {resto}.')

#Practica
#1. Operadores y expresiones
#1)
#a
1+1
#b
print(1.1 - 1.2)
#c
2*2
#d
6/3

#2)Concatenación de Cadenas
cadena1 = 'asd'

cadena2 = 'qwe'

cadena3 = cadena1 + cadena2
print(cadena3)

#3)Cálculo de Área de un Rectángulo
longitudRectangulo = 6
anchoRectangulo = 3
areaRectangulo = longitudRectangulo * anchoRectangulo
print(areaRectangulo)

#4)Cálculo de Interés Simple
def interes(principal,tasa,tiempo):
    resultado_interes = principal * tasa * tiempo
    return resultado_interes

principal = float(input('Ingrese el principal: '))
tasa = float(input('Ingrese la tasa: '))
tiempo = float(input('Ingrese el tiempo: '))

resultado_interes = interes(principal,tasa,tiempo)

print(f'El interes es de: {resultado_interes}.')

### modificado
def calcular_interes(principal, tasa, tiempo):
    """
    Calcula el interés simple.

    Args:
        principal (float): El monto principal.
        tasa (float): La tasa de interés (por ejemplo, 0.05 para el 5%).
        tiempo (float): El tiempo en años.

    Returns:
        float: El interés calculado.

    Raises:
        ValueError: Si alguno de los valores es negativo.
    """
    if principal < 0 or tasa < 0 or tiempo < 0:
        raise ValueError("Los valores deben ser positivos.")

    interes = principal * tasa * tiempo
    return round(interes, 2)

try:
    principal = float(input('Ingrese el principal: '))
    tasa = float(input('Ingrese la tasa (por ejemplo, 0.05 para el 5%): '))
    tiempo = float(input('Ingrese el tiempo en años: '))

    resultado_interes = calcular_interes(principal, tasa, tiempo)

    print(f'El interés es de: {resultado_interes}.')
except ValueError as e:
    print(f'Error: {e}')

#5)  Cálculo de Edad en Años Bisiestos
def edad_bisiestos(edad): 
    try:
        edad_bisiesta = edad // 4
        return edad_bisiesta
    except ZeroDivisionError:
        raise ValueError("La cantidad de años bisiestos no puede ser igual a cero")
try:   
    edad = int(input('Ingrese su edad: '))
    #anios_bisiestos = int(input('Ingrese la cantidad de años bisiestos: '))

    edad_bisiesta = edad_bisiestos(edad)
    print(f'{edad_bisiesta}')
except ValueError as e:
    print(f'Error: {e}')


#2. Controladores de flujo
#1)
#hecho por mi
numeros = [1,2,3,4,5,6]
def numeros_pares(numeros):
    pares = []
    for i in numeros:
        if i %2 == 0:
            pares.append(i)  
    return pares

pares = numeros_pares(numeros)
print(pares)
#echo por gpt
"""
def solicitar_numeros(mensaje):
    while True:
        try:
            numeros = int(input(mensaje))
            return numeros
        except ValueError:
            print("Por favor, ingresa un número valido")

def numeros_pares(numeros):
    pares = []
    for i in numeros:
        if i %2 == 0:
            pares.append(i)  
    return pares

cantidad_numeros = solicitar_numeros("cuantos números va a ingresar?")
numeros = []

for i in range(cantidad_numeros):
    numero = solicitar_numeros("Ingrese un número: ")
    numeros.append(numero)

pares = numeros_pares(numeros)
print(f'Los numeros {pares} son pares')
"""
#2)

edades = {
    "Lucas": 28,
    "Camila": 29,
    "Agustin": 27
}

for nombre, edad in edades.items():         #itera a través del diccionario edades utilizando el método .items(), 
    print(f'{nombre} tiene {edad} años')    #que nos permite acceder tanto a la clave (nombre) como al valor (edad) en cada iteración. 
    
#3)

numeros = [1,2,3,4,5,6]

suma = 0            

for i in numeros:
    if i %2 == 0:   # Si el numero es par True

        suma += i   # Sumamos i a la variable suma

print(suma)

#4)

palabras = ['hola','gato','pez']

for i in palabras:
    cantidad = len(i)

    print(i,cantidad)

#5)

estudiantes = {
    "Lucas": "A",
    "Camila": "B",
    "Agustin": "C"
}

for nombre, calificacion in estudiantes.items():
    print(f'{nombre} se saco {calificacion} en el examen')

#6)
frase = "La ciencia nunca resuelve un problema sin crear otros 10 más."

vocales = {
    "a":2,
    "e":1,
    "i":4,
    "0":0,
    "u":1
}

suma_vocales = 0

for i in frase:
    if i.lower() in vocales:
        suma_vocales += vocales[i.lower()]

print(f'La suma total de los valores de las vocales es {suma_vocales}')


#3.Entradas y Salidas de Datos

#1)Calculadora Simple

#Solicitamos al usuario que ingrese dos números
numero1= float(input("Ingrese el primer número: "))
numero2= float(input("Ingrese el segundo número: "))

#Le pedimos al usuario que ingrese la operación matemática
operacion = input("Ingrese la operacion matemática (+, -, *, /): ")

#Se realiza la operación
if operacion == "+":
    calculo = numero1 + numero2
elif operacion == "-":
    calculo = numero1 - numero2
elif operacion == "*":
    calculo = numero1 * numero2
elif operacion == "/":
    if numero2 != 0:
        calculo = numero1 / numero2
    else:
        calculo = "No es posible dividir por cero"
else:
    calculo = "No se puede realizar la operación"

#Mostramos el resultado
print(f'El resultado de la operación {operacion} entre {numero1} y {numero2} es: {calculo}')


#2) Conversión de Temperatura

#Se define funcion
def celsius_fahrenheit (temperatura):
    fahrenheit = (temperatura * 9/5)+32 #Se utiliza formula para pasar de grados Celsius a Fahrenheit
    return fahrenheit

#Se le pide al usuario una temperatura en grados Celsius
temperatura = float(input("Ingrese una temperatura en Celsius: "))

#Se utiliza función para pasar a Fahrenheit
fahrenheit = celsius_fahrenheit(temperatura)

print(f'La temperatura en fahrenheit es: {fahrenheit}')

#3)Suma de Números en la Línea de Comandos

import sys

numero1 = int(sys.argv[1])
numero2 = int(sys.argv[2])

suma = numero1 + numero2

print(f'La suma de {numero1} y {numero2} es {suma}')

#4) Generador de Saludos Personalizados

import sys

nombre = str(sys.argv[1])
print(f'Hola, {nombre}.¡Bienvenid@!')

#4. Funciones

#1) Función Simple de Suma
def suma(valor1, valor2):
    resultado = valor1 + valor2

    return resultado

numero1 = float(input('Ingrese un numero: '))
numero2 = float(input('Ingrese un numero: '))
resultado = suma(numero1,numero2)

print(f'El resultado de sumar {numero1} y {numero2} es {resultado}')

#2) Función que Devuelve Varios Valores

def dividir (valor1, valor2):
    resultado = valor1 / valor2
    residuo = valor1 % valor2
    return resultado, residuo

division = dividir(numero1,numero2)
print(f'El resultado de la division es {division[0]} y el resto es {division[1]}')

#3) Función con Argumentos Variables (*args)

def promedio(*args):
    suma = 0
    for i in args:
        suma += i
    resultado = suma/len(args)
    return suma, resultado
    
resultado1 = promedio(21,5,30,6,78)
print(f"La suma es {resultado1[0]} y el promedio es {resultado1[1]}")

#4) Función con Argumentos de Palabras Clave (**kwargs)

def informacion_persona(**kwargs):
    print(kwargs)
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')

informacion_persona(nombre='Pedro', edad=25, ciudad='Buenos Aires')


#5) Función que Modifica una Variable Global

contador = 0

def aumentar_contador(contador):
    return contador + 1
#se puede utilizar una funcion "global"?
contador = aumentar_contador(contador)
print (contador)

contador = aumentar_contador(contador)
print (contador)

contador = aumentar_contador(contador)
print (contador)

#6) Función que Utiliza Variables Locales y Globales
#preguntar
sufijo = 'able'

def combinar_cadenas():
    cadena = 'toma'
    combinada = cadena + sufijo
    return combinada


palabra = combinar_cadenas()
print(palabra)

#5. Excepciones

#1) Función para Calcular Promedio de Notas

estudiantes = {
    'Lucas':[8,6,4,10],
    'Agustin':[2,7,9,6],
    'Pedro':[8,3,5,9],
    'Julieta':[7,8,9,4],
    'Juan':[0,0,0,0]
}

def calcular_promedio(estudiantes):
    promedios = {}
    for estudiante, notas in estudiantes.items():
        try:
            promedio = sum(notas) / len(notas)
            promedios[estudiante] = promedio
        except ZeroDivisionError:
            promedios[estudiante] = 0
        except Exception as e:
            promedios[estudiante] = f'Error: {e}'
    return promedios

resultados = calcular_promedio(estudiantes)
print(resultados)

#2) Función para Filtrar Números Pares

numeros = [1,2,3,4,5,6,7,8,9,10,'f']

def filtrar_pares(numeros):
    pares=[]
    for i in numeros:
        try:
            if i %2 == 0:
                pares.append(i) 
        except Exception as e:
                print(f'Error: {e}')
        except ValueError:
                print(f'Error: {i} no es un numero')
    return pares

numeros_pares_p2 = filtrar_pares(numeros)
print(numeros_pares_p2) 

#3) Función para Combinar Listas de Compras

lista1 = ['qwe','asd','zxc']
lista2 = ['iop','qwe','bnm']

def combinar_listas(lista1, lista2):
   
    lista_combinada = list(lista1+lista2)
    lista_diccionario = {}
   
    for i in lista_combinada:
        cantidad_articulos = lista1.count(i) + lista2.count(i)
        lista_diccionario[i] = cantidad_articulos
   
    return lista_diccionario


print(combinar_listas(lista1,lista2)) 


#######1
frase = "Los string son cadenas de caracteres"
contador = 0
for letra in frase:
    contador += 1

print(contador)

######2
vocales = 'aeiou'
letra = ''
i= 0

while letra != 'o':
    letra = vocales[i]
    print(letra)
    i += 1

#####3
"""
if 'a' == 'b':
    print('A y B sin iguales')
elif:
    print('A y B son distintos')
"""
####5

def funcion10(tope):
    for i in range(1,tope):
        valor = {'indice':i, 'multi':i**i-1}

        if valor['indice'] > 3:
            return valor['multi']
        
        if valor['multi'] > 1:
            return valor['multi']
        
        return valor['multi']

funcion10(9)

####6

def buscar_dni_nuevo(dnis):
    for i in dnis:
        if i > 50000000:
            print('Hay un dni nuevo')
            return i
        return 999999999

dnis = ['34598712','59384756','57876543']
dni_nuevo = buscar_dni_nuevo(dnis)
print(dni_nuevo)


####7

def suma(*args):
    resultado ='0'
    for num in args:
        resultado += str(num)
    return resultado

resultado_final = suma(2, 4, 6, 8)
print(resultado_final)

####10

mi_lista = [1,2,'3',0]

def muchas_excepciones(mi_lista):
    for elemento in mi_lista:
        try:
            if elemento ==0:
                resultado = 10 / elemento
            elif elemento == 2:
                resultado = 10 / elemento
            else:
                resultado = 10 / elemento
            
            print(f'Resultado: {resultado}')
        except ZeroDivisionError:
            return elemento
        except TypeError:
            return resultado
        except NameError:
            return elemento
        except Exception as e:
            return e
    
    return elemento 

muchas_excepciones(mi_lista)