#1. Python Avanzado
#1)Operadores Encadenados
#a)

def comparar_numeros(n1, n2, n3):
    if n1 < n2 < n3:
        return True
    else:
        return False

n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))

resultado = comparar_numeros(n1, n2, n3)

if resultado:
    print("La cadena de comparaciones es verdadera.")
else:
    print("La cadena de comparaciones es falsa.")


#b)

def verificar_contrasena(contrasena):
    # Verificar la longitud de la contraseña
    if len(contrasena) >= 8:
        # Verificar si contiene al menos un número
        if any(caracter.isdigit() for caracter in contrasena):
            # Verificar si contiene al menos un carácter especial
            if any(caracter in "!@#$%^&*()_+[]{}|;':,.<>?/-" for caracter in contrasena):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

# Solicitar contraseña al usuario
contrasena = input("Ingrese una contraseña: ")

# Llamar a la función para verificar la contraseña
es_valida = verificar_contrasena(contrasena)

# Imprimir el resultado
if es_valida:
    print("La contraseña es válida.")
else:
    print("La contraseña no cumple con los criterios requeridos.")

#2) List Comprehension
#a)
numeros_pares = [x for x in range(2,21,2)]
print(numeros_pares)

#b)
palabras = ["asdasd","qweqweqwe","zxc"]
def palabras_mas_cinco(palabras):
    return [palabra for palabra in palabras if len(palabra) > 5]
        
nueva_lista = palabras_mas_cinco(palabras)
print(nueva_lista)

#3) Decoradores
#a)

import time

def medir_tiempo(func):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        tiempo_transcurrido = fin - inicio
        print(f"La función '{func.__name__}' tardó {tiempo_transcurrido} segundos en ejecutarse.")
        return resultado
    return envoltura

@medir_tiempo
def comparar_numeros(n1, n2, n3):
    if n1 < n2 < n3:
        return True
    else:
        return False
resultado = comparar_numeros(n1, n2, n3)
if resultado:
    print("La cadena de comparaciones es verdadera.")
else:
    print("La cadena de comparaciones es falsa.")