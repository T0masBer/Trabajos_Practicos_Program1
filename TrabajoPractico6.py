# Ejercicio 1

# Inicializamos una lista vacía para almacenar los números
import random
numeros = []

while True:
    # Solicitamos al usuario ingresar un número
    entrada = input("Ingresa un número (ingresa 0 para finalizar): ")

    # Verificamos si la entrada es un número válido
    if entrada.isdigit():
        numero = int(entrada)

        # Verificamos si el número es 0 para salir del bucle
        if numero == 0:
            break

        # Agregamos el número a la lista
        numeros.append(numero)
    else:
        print("Por favor, ingresa un número válido.")

# Mostramos la lista de números ingresados
print("Números ingresados:", numeros)


# Ejercicio 2

# Inicializamos una lista vacía para almacenar los números
numeros = []

while True:
    # Solicitamos al usuario ingresar un número
    entrada = input("Ingresa un número (ingresa 0 para finalizar): ")

    # Verificamos si la entrada es un número válido
    if entrada.isdigit():
        numero = int(entrada)

        # Verificamos si el número es 0 para salir del bucle
        if numero == 0:
            break

        # Agregamos el número a la lista
        numeros.append(numero)
    else:
        print("Por favor, ingresa un número válido.")

# Mostramos la lista de números ingresados
print("Números ingresados:", numeros)

# Solicitamos al usuario que ingrese un número para eliminar
numero_a_eliminar = int(input("Ingresa un número para eliminar de la lista: "))

# Verificamos si el número está en la lista y lo eliminamos
if numero_a_eliminar in numeros:
    numeros.remove(numero_a_eliminar)
    print(f"Se eliminó la primera ocurrencia de {
          numero_a_eliminar} de la lista.")
else:
    print(f"{numero_a_eliminar} no está en la lista. No se puede eliminar.")

# Mostramos la lista actualizada
print("Lista actualizada:", numeros)


# Ejercicio 3

# Inicializamos una lista vacía para almacenar los números
numeros = []

while True:
    # Solicitamos al usuario ingresar un número
    entrada = input("Ingresa un número (ingresa 0 para finalizar): ")

    # Verificamos si la entrada es un número válido
    if entrada.isdigit():
        numero = int(entrada)

        # Verificamos si el número es 0 para salir del bucle
        if numero == 0:
            break

        # Agregamos el número a la lista
        numeros.append(numero)
    else:
        print("Por favor, ingresa un número válido.")

# Mostramos la lista de números ingresados
print("Números ingresados:", numeros)

# Solicitamos al usuario que ingrese un número para eliminar
numero_a_eliminar = int(input("Ingresa un número para eliminar de la lista: "))

# Verificamos si el número está en la lista y lo eliminamos
if numero_a_eliminar in numeros:
    numeros.remove(numero_a_eliminar)
    print(f"Se eliminó la primera ocurrencia de {
          numero_a_eliminar} de la lista.")
else:
    print(f"{numero_a_eliminar} no está en la lista. No se puede eliminar.")

# Mostramos la lista actualizada
print("Lista actualizada:", numeros)

# Calculamos y mostramos la sumatoria de los números en la lista
sumatoria = sum(numeros)
print("Sumatoria de los números en la lista:", sumatoria)


# Ejercicio 4

# Inicializamos una lista vacía para almacenar los números
numeros = []

while True:
    # Solicitamos al usuario ingresar un número
    entrada = input("Ingresa un número (ingresa 0 para finalizar): ")

    # Verificamos si la entrada es un número válido
    if entrada.isdigit():
        numero = int(entrada)

        # Verificamos si el número es 0 para salir del bucle
        if numero == 0:
            break

        # Agregamos el número a la lista
        numeros.append(numero)
    else:
        print("Por favor, ingresa un número válido.")

# Mostramos la lista de números ingresados
print("Números ingresados:", numeros)

# Solicitamos al usuario que ingrese otro número
umbral = int(input("Ingresa otro número para crear la nueva lista: "))

# Creamos una nueva lista con elementos menores que el número dado
nueva_lista = [elemento for elemento in numeros if elemento < umbral]

# Mostramos la nueva lista e iteramos por ella
print(f"Elementos en la lista original menores que {umbral}:")
for elemento in nueva_lista:
    print(elemento)

# Ejercicio 5

# Inicializamos una lista vacía para almacenar los números
numeros = []

while True:
    # Solicitamos al usuario ingresar un número
    entrada = input("Ingresa un número (ingresa 0 para finalizar): ")

    # Verificamos si la entrada es un número válido
    if entrada.isdigit():
        numero = int(entrada)

        # Verificamos si el número es 0 para salir del bucle
        if numero == 0:
            break

        # Agregamos el número a la lista
        numeros.append(numero)
    else:
        print("Por favor, ingresa un número válido.")

# Mostramos la lista de números ingresados
print("Números ingresados:", numeros)

# Creamos un diccionario para realizar un seguimiento de la cantidad de veces que aparece cada número
contador_numeros = {}

for numero in numeros:
    if numero in contador_numeros:
        contador_numeros[numero] += 1
    else:
        contador_numeros[numero] = 1

# Convertimos el diccionario en una lista de tuplas
lista_tuplas = list(contador_numeros.items())

# Mostramos la nueva lista de tuplas
print("Nueva lista de tuplas:", lista_tuplas)


# Ejercicio 6

# Inicializamos conjuntos vacíos para los nombres de nivel primario y secundario
nombres_primario = set()
nombres_secundario = set()

# Solicitamos nombres de alumnos de nivel primario
print("Ingresa los nombres de los alumnos de nivel primario (ingresa 'x' para finalizar):")
while True:
    nombre_primario = input()
    if nombre_primario.lower() == 'x':
        break
    nombres_primario.add(nombre_primario)

# Solicitamos nombres de alumnos de nivel secundario
print("Ingresa los nombres de los alumnos de nivel secundario (ingresa 'x' para finalizar):")
while True:
    nombre_secundario = input()
    if nombre_secundario.lower() == 'x':
        break
    nombres_secundario.add(nombre_secundario)

# a. Informar los nombres de todos los alumnos sin repeticiones
todos_los_nombres = nombres_primario.union(nombres_secundario)
print("\nNombres de todos los alumnos sin repeticiones:")
for nombre in todos_los_nombres:
    print(nombre)

# b. Informar qué nombres se repiten
nombres_repetidos = nombres_primario.intersection(nombres_secundario)
print("\nNombres que se repiten entre nivel primario y secundario:")
for nombre in nombres_repetidos:
    print(nombre)

# c. Informar qué nombres de nivel primario no se repiten en secundario
nombres_primario_no_repetidos = nombres_primario.difference(nombres_secundario)
print("\nNombres de nivel primario que no se repiten en secundario:")
for nombre in nombres_primario_no_repetidos:
    print(nombre)

# Ejercicio 7

# Inicializamos un diccionario para realizar un seguimiento de las ocurrencias de cada carácter
ocurrencias_caracteres = {}

# Procesamos 50 strings ingresados por el usuario
for _ in range(50):
    string_ingresado = input(
        "Ingresa un string (presiona Enter para continuar): ")

    # Actualizamos el diccionario con las ocurrencias de cada carácter
    for caracter in string_ingresado:
        if caracter in ocurrencias_caracteres:
            ocurrencias_caracteres[caracter] += 1
        else:
            ocurrencias_caracteres[caracter] = 1

# Mostramos la cantidad total de ocurrencias de cada carácter
print("\nCantidad total de ocurrencias de cada carácter:")
for caracter, cantidad in ocurrencias_caracteres.items():
    print(f"'{caracter}': {cantidad}")

# Ejercicio 8

# Inicializamos listas para almacenar los resultados de cada equipo
triunfos = [0] * 10
empates = [0] * 10
derrotas = [0] * 10
diferencia_goles = [0] * 10
puntos = [0] * 10

# Procesamos los goles y calculamos los resultados
for equipo_local in range(10):
    for equipo_visitante in range(10):
        if equipo_local != equipo_visitante:
            goles_local = goles[equipo_local][equipo_visitante]
            goles_visitante = goles[equipo_visitante][equipo_local]

            if goles_local > goles_visitante:
                triunfos[equipo_local] += 1
            elif goles_local < goles_visitante:
                derrotas[equipo_local] += 1
            else:
                empates[equipo_local] += 1

            diferencia_goles[equipo_local] += goles_local - goles_visitante

# Calculamos los puntos para cada equipo (3 puntos por triunfo, 1 punto por empate)
for i in range(10):
    puntos[i] = triunfos[i] * 3 + empates[i]

# Mostramos los resultados
for i in range(10):
    print(f"Equipo {i + 1}: Triunfos={triunfos[i]}, Empates={empates[i]}, Derrotas={
          derrotas[i]}, Diferencia de Goles={diferencia_goles[i]}, Puntos={puntos[i]}")


# Ejercicio 9


def inicializar_tablero(filas, columnas):
    # Creamos una matriz para representar el tablero
    tablero = [[' ' for _ in range(columnas)] for _ in range(filas)]
    return tablero


def colocar_parejas(tablero, simbolos):
    # Duplicamos los símbolos para formar parejas
    parejas = simbolos * 2
    random.shuffle(parejas)

    # Colocamos las parejas en el tablero
    for fila in range(len(tablero)):
        for columna in range(len(tablero[0])):
            tablero[fila][columna] = parejas.pop()


def imprimir_tablero(tablero, reveladas):
    # Imprimimos el tablero, revelando las cartas que corresponden
    for fila in range(len(tablero)):
        for columna in range(len(tablero[0])):
            if (fila, columna) in reveladas:
                print(tablero[fila][columna], end=' ')
            else:
                print('X', end=' ')
        print()


def jugar():
    filas = 4
    columnas = 4
    simbolos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    tablero = inicializar_tablero(filas, columnas)
    colocar_parejas(tablero, simbolos)

    reveladas = set()
    intentos = 0

    while len(reveladas) < filas * columnas:
        imprimir_tablero(tablero, reveladas)

        # Solicitamos al jugador que ingrese las coordenadas de dos cartas
        fila1 = int(input("Ingresa la fila de la primera carta: ")) - 1
        columna1 = int(input("Ingresa la columna de la primera carta: ")) - 1

        fila2 = int(input("Ingresa la fila de la segunda carta: ")) - 1
        columna2 = int(input("Ingresa la columna de la segunda carta: ")) - 1

        if (fila1, columna1) == (fila2, columna2) or (fila1, columna1) in reveladas or (fila2, columna2) in reveladas:
            print("¡Movimiento inválido! Por favor, elige cartas diferentes.")
        elif tablero[fila1][columna1] == tablero[fila2][columna2]:
            print("¡Encontraste una pareja!")
            reveladas.add((fila1, columna1))
            reveladas.add((fila2, columna2))
        else:
            print("¡Intento incorrecto!")

        intentos += 1

    print(f"Felicitaciones, ¡has encontrado todas las parejas en {
          intentos} intentos!")

# Ejercicio 10


def obtener_diagonal_principal(matriz):
    # La diagonal principal consiste en los elementos en la posición [i][i]
    diagonal_principal = [matriz[i][i] for i in range(len(matriz))]
    return diagonal_principal


def obtener_diagonal_inversa(matriz):
    # La diagonal inversa consiste en los elementos en la posición [i][n-i-1]
    diagonal_inversa = [matriz[i][len(matriz) - i - 1]
                        for i in range(len(matriz))]
    return diagonal_inversa


# Ejemplo de uso
matriz_cuadrada = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# a. Obtener la diagonal principal
diagonal_principal = obtener_diagonal_principal(matriz_cuadrada)
print("Diagonal principal:", diagonal_principal)

# b. Obtener la diagonal inversa
diagonal_inversa = obtener_diagonal_inversa(matriz_cuadrada)
print("Diagonal inversa:", diagonal_inversa)


# Ejercicio 11

# Definimos el diccionario de divisas y sus símbolos
diccionario_divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}

# Solicitamos al usuario que ingrese una divisa
divisa = input("Ingresa una divisa: ")

# Verificamos si la divisa está en el diccionario
if divisa in diccionario_divisas:
    simbolo = diccionario_divisas[divisa]
    print(f"El símbolo de {divisa} es {simbolo}.")
else:
    print(f"La divisa {divisa} no está en el diccionario.")


# Ejercicio 12

# Solicitamos al usuario que ingrese su información
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
direccion = input("Ingresa tu dirección: ")
telefono = input("Ingresa tu número de teléfono: ")

# Creamos un diccionario con la información proporcionada
informacion_usuario = {
    'Nombre': nombre,
    'Edad': edad,
    'Dirección': direccion,
    'Teléfono': telefono
}

# Mostramos la información por pantalla
mensaje = f"{informacion_usuario['Nombre']} tiene {informacion_usuario['Edad']} años, vive en {
    informacion_usuario['Dirección']} y su número de teléfono es {informacion_usuario['Teléfono']}."
print(mensaje)


# Ejercicio 13

# Definimos el diccionario de precios de frutas
precios_frutas = {'Manzana': 1.5, 'Banana': 0.8,
                  'Uva': 2.0, 'Naranja': 1.2, 'Pera': 1.8}

# Solicitamos al usuario que ingrese la fruta y la cantidad de kilos
fruta = input("Ingresa el nombre de la fruta: ")
kilos = float(input("Ingresa la cantidad de kilos: "))

# Verificamos si la fruta está en el diccionario de precios
if fruta in precios_frutas:
    precio_total = precios_frutas[fruta] * kilos
    print(f"El precio de {kilos} kilos de {fruta} es: {precio_total} euros.")
else:
    print(f"Lo siento, la fruta {fruta} no está en el diccionario de precios.")
