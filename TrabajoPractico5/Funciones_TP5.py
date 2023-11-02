import math
#Funcion ejercicio 1
def val_dni (num):
    if len(num) == 7 or len(num) == 8:
        return True
    else:
        return False

#Funcion ejercicio 2

def last_word(phrs):
    word = phrs.split()

    if len(word) > 0:
        l_word = word[-1]
        return l_word   
    else:
        return 0

#Funcion ejercicio 3

def get_ID(full_name, dni):
    if not (len(dni) == 7 or len(dni) == 8) or not dni.isdigit():
        return None
    
    words = full_name.split()

    first_name = words[0]
    last_name = words[-1]
    identifier = first_name.capitalize() + str(len(last_name)) + dni[:3]
    return identifier

#Funcion ejercicio 4

def multiplos (num1,num2):
    
    if num1 % num2 == 0:
        print(f'El numero {num1} es multiplo de {num2}')
    else:
        print(f'El numero {num1} no es multiplo de {num2}')

#Funcion ejercicio 5

def calc_med_temp(temp_max,temp_min):
    med_tmp = (temp_max + temp_min) / 2
    return med_tmp

#Funcion ejercicio 6

def add_spaces(text):
    spaced_text = " ".join(text)
    return spaced_text

#Funcion Ejercicio 7

def find_max_min (list):
    if len(list) == 0:
        return None
    
    max = min = list[0]

    for value in list:
        if value > max:
            max = value
        elif value < min:
            min = value
    
    return max,min

#Funcion ejercicio 8

def area_per(rad):

    per_c = (rad * 2) * 3.1416
    area_c = (rad ** 2) * 3.1416
    return per_c, area_c

#Funcion ejercicio 9

def login(user_name,password):
    if user_name == 'usuario1' and password == 'asdasd':
        return True
    else:
        return False
    
#Funcion Ejercicio 10

def apply_discount(carrito):
    final_price = 0

    for producto, price in carrito.items():
        descuento = price * (carrito[producto] / 100)  
        final_price += price - descuento  

    return final_price

#Funcion Ejercicio 11 

def apply_function_to_list(function, lis):
    result = []
    for element in list:
        result.append(function(element))
    return result

#Funcion ejercicio 12

def get_lenght_words(phrase):
    words = phrase.split() 
    length_words = {}

    for word in words:
        length_words[word] = len(word)

    return length_words

#Funcion ejercicio 13

def calcular_modulo_vector(vector):
    suma_cuadrados = sum(x ** 2 for x in vector)
    modulo = math.sqrt(suma_cuadrados)
    return modulo

#Funcion ejercicio 14

def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

#Funciones ejercicio 15

def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

def leer_numeros_y_mostrar_factoriales():
    cantidad_total_numeros = 0

    while True:
        try:
            numero = int(input("Ingrese un número (o 0 para finalizar): "))

            if numero == 0:
                break

            factorial = calcular_factorial(numero)
            print(f"El factorial de {numero} es {factorial}")

            cantidad_total_numeros += 1

        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    return cantidad_total_numeros

#Funcion ejercicio 16

def calcular_frecuencia_digito(numero, digito):
    
    numero_str = str(numero)
   
    ocurrencias = 0
  
    for d in numero_str:
        if d == str(digito):
            ocurrencias += 1
    return ocurrencias

#Funciones ejercicio 17

def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def calcular_suma_digitos(numero):
    suma = 0
    while numero > 0:
        digito = numero % 10
        suma += digito
        numero //= 10
    return suma

def calcular_frecuencia_digito(numero, digito):
    numero_str = str(numero)
    frecuencia = numero_str.count(str(digito))
    return frecuencia

def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

mayor_primo = None
mayor_primo_factorial = 1
