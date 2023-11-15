# Ejercicio 1

def contar_digitos(n):
    # Convertimos el número a cadena para facilitar la manipulación de los dígitos
    n_str = str(n)

    # Devolvemos la longitud de la cadena, que es la cantidad de dígitos
    return len(n_str)


# Ejemplo de uso
numero = int(input("Ingresa un número positivo: "))

if numero >= 0:
    cantidad_digitos = contar_digitos(numero)
    print(f"El número {numero} tiene {cantidad_digitos} dígitos.")
else:
    print("Por favor, ingresa un número positivo.")

# Ejercicio 2


def es_potencia(n, b):
    # Verificamos si n es una potencia de b
    if n == 1:
        return True
    elif n < b:
        return False
    else:
        # Continuamos dividiendo n por b hasta que n sea menor que b
        while n % b == 0:
            n //= b
        return n == 1


# Ejemplo de uso
numero = int(input("Ingresa un número: "))
base = int(input("Ingresa la base: "))

resultado = es_potencia(numero, base)

if resultado:
    print(f"{numero} es una potencia de {base}.")
else:
    print(f"{numero} no es una potencia de {base}.")

# Ejercicio 3


def encontrar_posiciones(a, b, index=0, resultados=None):
    # Inicializamos la lista de resultados en la primera llamada recursiva
    if resultados is None:
        resultados = []

    # Encontramos la próxima ocurrencia de b en a
    pos = a.find(b, index)

    # Si encontramos una ocurrencia, la agregamos a la lista de resultados
    if pos != -1:
        resultados.append(pos)

        # Llamamos recursivamente a la función para buscar más ocurrencias
        return encontrar_posiciones(a, b, pos + 1, resultados)
    else:
        # Devolvemos la lista de resultados
        return resultados


# Ejemplo de uso
cadena_a = "abababab"
cadena_b = "ab"

posiciones = encontrar_posiciones(cadena_a, cadena_b)
print(f"Las posiciones de '{cadena_b}' en '{cadena_a}' son: {posiciones}")

# Ejercicio 4


def par(n):
    if n == 0:
        return True  # El cero se considera par
    else:
        return impar(n - 1)


def impar(n):
    if n == 0:
        return False  # El cero se considera par
    else:
        return par(n - 1)


# Ejemplo de uso
numero = int(input("Ingresa un número natural: "))

if par(numero):
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")

# Ejercicio 5


def encontrar_mayor(lista):
    # Caso base: si la lista está vacía, no hay mayor elemento
    if not lista:
        return None

    # Caso base: si la lista tiene un solo elemento, ese es el mayor
    if len(lista) == 1:
        return lista[0]

    # Llamada recursiva para encontrar el mayor entre el primer elemento y el resto de la lista
    mayor_restante = encontrar_mayor(lista[1:])

    # Comparamos el mayor del resto con el primer elemento
    return lista[0] if lista[0] > mayor_restante else mayor_restante


# Ejemplo de uso
numeros = [12, 45, 78, 23, 56, 89, 34]

mayor = encontrar_mayor(numeros)
print(f"El mayor elemento de la lista es: {mayor}")

# Ejercicio 6


def replicar_elementos(lista, n):
    # Caso base: si la lista está vacía o n es 0, retornamos una lista vacía
    if not lista or n == 0:
        return []

    # Llamada recursiva para replicar los elementos de la lista n-1 veces
    replicacion_resto = replicar_elementos(lista, n - 1)

    # Devolvemos la lista original replicada n veces
    return lista + replicacion_resto


# Ejemplo de uso
original = [1, 3, 3, 7]
replicada = replicar_elementos(original, 2)

print(f"Lista original: {original}")
print(f"Lista replicada: {replicada}")

# Ejercicio 7


def sumatoria_recursiva(n, p):
    # Caso base: si n es 1, retornamos p
    if n == 1:
        return p
    else:
        # Llamada recursiva para calcular la sumatoria
        return n * p + sumatoria_recursiva(n - 1, p)


# Solicitar al usuario que ingrese los valores de n y p
n = int(input("Ingrese el valor de n: "))
p = int(input("Ingrese el valor de p: "))

# Calcular y mostrar el resultado de K(n, p) usando la función recursiva
resultado = sumatoria_recursiva(n, p)
print(f"El resultado de K({n}, {p}) es: {resultado}")

# Ejercicio 8


def pascal(n, k):
    # Caso base: los bordes del triángulo son siempre 1
    if k == 0 or k == n:
        return 1
    else:
        # Llamada recursiva para calcular el valor en la posición actual
        return pascal(n - 1, k - 1) + pascal(n - 1, k)


# Ejemplo de uso
fila = int(input("Ingrese el número de fila (n): "))
columna = int(input("Ingrese el número de columna (k): "))

# Calcular y mostrar el valor en la posición (n, k) del Triángulo de Pascal
resultado = pascal(fila, columna)
print(f"El valor en la posición ({fila}, {
      columna}) del Triángulo de Pascal es: {resultado}")

# Ejercicio 9


def combinaciones(lista, k, prefijo=""):
    # Caso base: si la longitud del prefijo es igual a k, imprimimos el prefijo
    if len(prefijo) == k:
        print(prefijo)
        return

    # Llamada recursiva para generar las combinaciones
    for caracter in lista:
        combinaciones(lista, k, prefijo + caracter)


# Ejemplo de uso
caracteres = input("Ingrese una lista de caracteres únicos (sin espacios): ")
k = int(input("Ingrese la longitud de las combinaciones (k): "))

# Verificar que la entrada sea válida
if len(set(caracteres)) == len(caracteres):
    # Llamar a la función para generar las combinaciones
    combinaciones(caracteres, k)
else:
    print("La lista de caracteres debe contener únicamente caracteres únicos.")


# Ejercicio 10

def medidas_hoja_A(N):
    # Caso base: A0 tiene medidas fijas
    if N == 0:
        return (841, 1189)

    # Llamada recursiva para calcular medidas de A(N-1)
    ancho_anterior, largo_anterior = medidas_hoja_A(N - 1)

    # Calcular medidas de A(N) doblando al medio las de A(N-1)
    ancho_actual = largo_anterior
    largo_actual = ancho_anterior / 2

    # Redondear a números enteros
    ancho_actual = round(ancho_actual)
    largo_actual = round(largo_actual)

    return (ancho_actual, largo_actual)


# Ejemplo de uso
N = int(input("Ingrese el valor de N (mayor que cero): "))

if N > 0:
    medidas = medidas_hoja_A(N)
    print(f"Las medidas de la hoja A({N}) son: {medidas}")
else:
    print("Por favor, ingrese un valor de N mayor que cero.")
