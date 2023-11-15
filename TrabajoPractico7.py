# Ejercicio 1

def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


# Ejemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90]
ordenamiento_burbuja(numeros)
print("Lista ordenada:", numeros)

# Ejercicio 2


def ordenamiento_seleccion(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]


# Ejemplo de uso
palabras = ["banana", "manzana", "pera", "uva", "kiwi"]
ordenamiento_seleccion(palabras)
print("Lista ordenada:", palabras)

# Ejercicio 3

libros = [
    {'titulo': 'Libro C', 'autor': 'Autor C', 'año': 2005},
    {'titulo': 'Libro A', 'autor': 'Autor A', 'año': 2000},
    {'titulo': 'Libro B', 'autor': 'Autor B', 'año': 2010}
]

libros_ordenados = sorted(libros, key=lambda x: x['año'])
print("Libros ordenados por año de publicación:", libros_ordenados)

# Ejercicio 4


def ordenamiento_insercion_por_longitud(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and len(actual) < len(lista[j]):
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual


# Ejemplo de uso
cadenas = ["manzana", "banana", "uva", "kiwi", "pera"]
ordenamiento_insercion_por_longitud(cadenas)
print("Lista ordenada por longitud:", cadenas)

# Ejercicio 5

numeros_descendentes = sorted(numeros, reverse=True)
print("Lista ordenada en orden descendente:", numeros_descendentes)

# Ejercicio 6


def ordenamiento_por_conteo(lista):
    min_num, max_num = min(lista), max(lista)
    conteo = [0] * (max_num - min_num + 1)

    for num in lista:
        conteo[num - min_num] += 1

    resultado = []
    for i in range(len(conteo)):
        resultado.extend([i + min_num] * conteo[i])

    return resultado


# Ejemplo de uso
numeros = [4, 2, 3, 4, 1, 2, 5, 3, 1]
numeros_ordenados = ordenamiento_por_conteo(numeros)
print("Lista ordenada por conteo:", numeros_ordenados)

# Ejercicio 7

lista_mixta = [3, "kiwi", 1, "banana", 2, "manzana"]
numeros_ordenados = sorted(
    [elemento for elemento in lista_mixta if isinstance(elemento, int)])
cadenas_ordenadas = sorted(
    [elemento for elemento in lista_mixta if isinstance(elemento, str)])
lista_mixta_ordenada = numeros_ordenados + cadenas_ordenadas
print("Lista mixta ordenada:", lista_mixta_ordenada)

# Ejercicio 8


def merge_sort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1


# Ejemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90]
merge_sort(numeros)
print("Lista ordenada con Merge Sort:", numeros)
