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