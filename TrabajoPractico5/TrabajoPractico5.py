<<<<<<< HEAD
from Funciones_TP5 import *
import math


#Ejercicio 1

print('Por favor ingrese su dni')
dni = input()

if val_dni(dni) == True:
    print('Su dni es valido')
else:
    print('Su dni no es valido')

#Ejercicio 2

print('Ingrese una frase')
phrase = input() 
print(f'La ultima palabra de la frase ingresada es: {last_word(phrase)}')

#Ejercicio 3

while True:
    print('Ingrese nombre completo y apellido del socio')
    print('Para salir ingrese un nombre vacio')
    name = input()

    if name == '':
        break
    
    print('Ingrese el dni del socio')
    dni = input()
    full_identifier = get_ID(name,dni)

    if full_identifier:
        print("ID = ",full_identifier)
    else:
        print('El numero de dni ingresado es incorrecto')

#Ejercicio 4

print('Ingrese 2 numeros')
num1 = int(input('Primer numero '))
num2 = int(input('Segundo numero '))

print(multiplos(num1,num2))

#Ejercicio 5

num_days = int(input('Ingrese el numero de dias'))

for day in range(1, num_days +1 ):
    maximun_temperature = int(input(f'Ingrese la temeperatura maxima del dia {day}: '))
    minimun_temperature = int(input(f'Ingrese la temeperatura minima del dia {day}: '))

    medium_temperature = calc_med_temp(maximun_temperature,minimun_temperature)
    print(f'La temperatura media del dia {day} es: {medium_temperature:.2f} grados Celcius')

#Ejercicio 6

original_text = input('Ingrese el texto: ')
spaced_text = add_spaces(original_text)
print(f'El texto queda de la sig forma: {spaced_text}')

#Ejercicio 7

nums = []

while True:
    entrance = input('Ingrese un numero (o ingrese q para salir)')

    if entrance.lower == 'q':
        break

    try:
        entrance = float(entrance)
        nums.append[entrance]
    except ValueError:
        print('Por favor, ingrese un numero valido')
    
max_num, min_num = find_max_min(entrance)

if max_num is not None and min_num is not None:
    print('El numero maximo es ',max_num)
    print('El numero minimo es ',min_num)
else:
    print('No se ingresaron numeros validos')

#Ejercicio 8

radius = float(input('Ingrese el radio del circulo '))

per, area = area_per(radius)
print(f'El perimetro del circulo es {per}, y su area es {area}')

#Ejercicio 9

tries = 0

while tries < 3:

    name = input('Nombre de usuario: ')
    passw = input('Contraseña: ')

    if login(name,passw):
        print('Inicio de sesion exitoso')
        break
    else:
        print('Nombre de usuarioo o contraseña incorrectos')
        tries += 1
    
    if tries == 3:
        print('Has alcanzado el numero maximo de intentos. Fin del programa')
    

#Ejercicio 10

# Ejemplo de uso

carrito_de_compra = {
    "producto1": 100,
    "producto2": 50,
    "producto3": 75
}

descuentos = {
    "producto1": 10,
    "producto2": 20,
    "producto3": 15
}

precio_final = apply_discount(carrito_de_compra, descuentos)
print("Precio final de la compra:", precio_final)


#Ejercicio 11

def cuadrado(x):
    return x ** 2

lista_numeros = [1, 2, 3, 4, 5]
resultados = apply_function_to_list(cuadrado, lista_numeros)
print(resultados)

#Ejercicio 12

# Ejemplo de uso:
frase = "Esta es una frase de ejemplo"
resultados = get_lenght_words(frase)
print(resultados)

#Ejercicio 13

# Ejemplo de uso con un vector en 2D
vector_2d = (3, 4)  
modulo_2d = calcular_modulo_vector(vector_2d)
print("Módulo del vector en 2D:", modulo_2d)

# Ejemplo de uso con un vector en 3D
vector_3d = (1, 2, 3)  
modulo_3d = calcular_modulo_vector(vector_3d)
print("Módulo del vector en 3D:", modulo_3d)


#Ejercicio 14

try:
    numero = int(input("Ingrese un número entero: "))
    if es_primo(numero):
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")
except ValueError:
    print("Por favor, ingrese un número entero válido.")


#Ejercicio 15

total_numeros = leer_numeros_y_mostrar_factoriales()
print(f"Cantidad total de números leídos: {total_numeros}")


#Ejercicio 16

try:
    numero = int(input("Ingrese un número entero: "))
    digito = int(input("Ingrese un dígito para contar: "))

    frecuencia = calcular_frecuencia_digito(numero, digito)
    print(f"El dígito {digito} aparece {frecuencia} veces en el número {numero}.")
except ValueError:
    print("Por favor, ingrese un número entero y un dígito válido.")


#Ejercicio 17


while True:
    try:
        numero = int(input("Ingrese un número primo (o cualquier número no primo para finalizar): "))
        
        if not es_primo(numero):
            break
        
        if numero > mayor_primo:
            mayor_primo = numero
            mayor_primo_factorial = calcular_factorial(numero)

        suma_digitos = calcular_suma_digitos(numero)
        print(f"Suma de los dígitos del número {numero}: {suma_digitos}")

        digito = int(input("Ingrese un dígito para contar su frecuencia: "))
        frecuencia = calcular_frecuencia_digito(numero, digito)
        print(f"El dígito {digito} aparece {frecuencia} veces en el número {numero}.")
    
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if mayor_primo is not None:
    print(f"El factorial del mayor número primo ingresado ({mayor_primo}) es: {mayor_primo_factorial}")
else:
=======
from Funciones_TP5 import *
import math


#Ejercicio 1

print('Por favor ingrese su dni')
dni = input()

if val_dni(dni) == True:
    print('Su dni es valido')
else:
    print('Su dni no es valido')

#Ejercicio 2

print('Ingrese una frase')
phrase = input() 
print(f'La ultima palabra de la frase ingresada es: {last_word(phrase)}')

#Ejercicio 3

while True:
    print('Ingrese nombre completo y apellido del socio')
    print('Para salir ingrese un nombre vacio')
    name = input()

    if name == '':
        break
    
    print('Ingrese el dni del socio')
    dni = input()
    full_identifier = get_ID(name,dni)

    if full_identifier:
        print("ID = ",full_identifier)
    else:
        print('El numero de dni ingresado es incorrecto')

#Ejercicio 4

print('Ingrese 2 numeros')
num1 = int(input('Primer numero '))
num2 = int(input('Segundo numero '))

print(multiplos(num1,num2))

#Ejercicio 5

num_days = int(input('Ingrese el numero de dias'))

for day in range(1, num_days +1 ):
    maximun_temperature = int(input(f'Ingrese la temeperatura maxima del dia {day}: '))
    minimun_temperature = int(input(f'Ingrese la temeperatura minima del dia {day}: '))

    medium_temperature = calc_med_temp(maximun_temperature,minimun_temperature)
    print(f'La temperatura media del dia {day} es: {medium_temperature:.2f} grados Celcius')

#Ejercicio 6

original_text = input('Ingrese el texto: ')
spaced_text = add_spaces(original_text)
print(f'El texto queda de la sig forma: {spaced_text}')

#Ejercicio 7

nums = []

while True:
    entrance = input('Ingrese un numero (o ingrese q para salir)')

    if entrance.lower == 'q':
        break

    try:
        entrance = float(entrance)
        nums.append[entrance]
    except ValueError:
        print('Por favor, ingrese un numero valido')
    
max_num, min_num = find_max_min(entrance)

if max_num is not None and min_num is not None:
    print('El numero maximo es ',max_num)
    print('El numero minimo es ',min_num)
else:
    print('No se ingresaron numeros validos')

#Ejercicio 8

radius = float(input('Ingrese el radio del circulo '))

per, area = area_per(radius)
print(f'El perimetro del circulo es {per}, y su area es {area}')

#Ejercicio 9

tries = 0

while tries < 3:

    name = input('Nombre de usuario: ')
    passw = input('Contraseña: ')

    if login(name,passw):
        print('Inicio de sesion exitoso')
        break
    else:
        print('Nombre de usuarioo o contraseña incorrectos')
        tries += 1
    
    if tries == 3:
        print('Has alcanzado el numero maximo de intentos. Fin del programa')
    

#Ejercicio 10

# Ejemplo de uso

carrito_de_compra = {
    "producto1": 100,
    "producto2": 50,
    "producto3": 75
}

descuentos = {
    "producto1": 10,
    "producto2": 20,
    "producto3": 15
}

precio_final = apply_discount(carrito_de_compra, descuentos)
print("Precio final de la compra:", precio_final)


#Ejercicio 11

def cuadrado(x):
    return x ** 2

lista_numeros = [1, 2, 3, 4, 5]
resultados = apply_function_to_list(cuadrado, lista_numeros)
print(resultados)

#Ejercicio 12

# Ejemplo de uso:
frase = "Esta es una frase de ejemplo"
resultados = get_lenght_words(frase)
print(resultados)

#Ejercicio 13

# Ejemplo de uso con un vector en 2D
vector_2d = (3, 4)  
modulo_2d = calcular_modulo_vector(vector_2d)
print("Módulo del vector en 2D:", modulo_2d)

# Ejemplo de uso con un vector en 3D
vector_3d = (1, 2, 3)  
modulo_3d = calcular_modulo_vector(vector_3d)
print("Módulo del vector en 3D:", modulo_3d)


#Ejercicio 14

try:
    numero = int(input("Ingrese un número entero: "))
    if es_primo(numero):
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")
except ValueError:
    print("Por favor, ingrese un número entero válido.")


#Ejercicio 15

total_numeros = leer_numeros_y_mostrar_factoriales()
print(f"Cantidad total de números leídos: {total_numeros}")


#Ejercicio 16

try:
    numero = int(input("Ingrese un número entero: "))
    digito = int(input("Ingrese un dígito para contar: "))

    frecuencia = calcular_frecuencia_digito(numero, digito)
    print(f"El dígito {digito} aparece {frecuencia} veces en el número {numero}.")
except ValueError:
    print("Por favor, ingrese un número entero y un dígito válido.")


#Ejercicio 17


while True:
    try:
        numero = int(input("Ingrese un número primo (o cualquier número no primo para finalizar): "))
        
        if not es_primo(numero):
            break
        
        if numero > mayor_primo:
            mayor_primo = numero
            mayor_primo_factorial = calcular_factorial(numero)

        suma_digitos = calcular_suma_digitos(numero)
        print(f"Suma de los dígitos del número {numero}: {suma_digitos}")

        digito = int(input("Ingrese un dígito para contar su frecuencia: "))
        frecuencia = calcular_frecuencia_digito(numero, digito)
        print(f"El dígito {digito} aparece {frecuencia} veces en el número {numero}.")
    
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if mayor_primo is not None:
    print(f"El factorial del mayor número primo ingresado ({mayor_primo}) es: {mayor_primo_factorial}")
else:
>>>>>>> f917c948bd4d7f288a748041ebf67e07c17dc9de
    print("No se ingresaron números primos.")