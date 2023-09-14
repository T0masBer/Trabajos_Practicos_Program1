#Ejercicio 1
x = 0

while x < 30:
    if x == 15:
        print("Se rompio la ejecucion del bucle cuando x valia: ", x)
        break
    
    if x in (4, 6, 10):
        print("Se salto el valor", x, "de x ")
    else:
        print(x)
    
    x += 1

#Ejercicio 2

while True:
    linea = input("Ingrese una línea (o deje en blanco para salir): ")
    if linea == "":
        break
    else:
        print(linea.upper())

print("Programa finalizado.")

#Ejercico 3

saldo = 0
bitacora = []

while True:
    print("\nSeleccione una opción:")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Mostrar saldo")
    print("4. Mostrar bitácora")
    print("5. Salir")

    opcion = input("Ingrese el número de opción: ")

    if opcion == "1":
        monto = float(input("Ingrese el monto a depositar: "))
        saldo += monto
        bitacora.append(f"D {monto}")
        print("Depósito realizado.")

    elif opcion == "2":
        monto = float(input("Ingrese el monto a retirar: "))
        if monto <= saldo:
            saldo -= monto
            bitacora.append(f"R {monto}")
            print("Retiro realizado.")
        else:
            print("Saldo insuficiente para realizar el retiro.")

    elif opcion == "3":
        print(f"Saldo actual: {saldo}")

    elif opcion == "4":
        print("Bitácora de operaciones:")
        for operacion in bitacora:
            print(operacion)

    elif opcion == "5":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")

#Ejercicio 4

contador_primos = 0

while True:
    entrada = int(input("Ingrese un número mayor que 1 (o 0 para finalizar): "))
    if entrada == 0:
        break
    if entrada <= 1:
        continue  # Ignorar números menores o iguales a 1

    es_primo = True
    for i in range(2, entrada):
        if entrada % i == 0:
            es_primo = False
            break

    if es_primo:
        contador_primos += 1

print(f"La cantidad de números primos ingresados es: {contador_primos}")

#Ejercicio 5

# Solicitar al usuario dos años
año_inicial = int(input("Ingrese el año inicial: "))
año_final = int(input("Ingrese el año final: "))

# Iterar a través del rango de años
for año in range(año_inicial, año_final + 1):
    # Verificar si el año es bisiesto y múltiplo de 10
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        if año % 10 == 0:
            print(año)

#Ejercicio 6

for numero in range(1, 21):
    if numero % 2 != 0:  # Verificar si el número es impar
        continue  # Omitir números impares
    print(numero)

#Ejercicio 7

# Crear una lista de números
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Número que queremos encontrar
numero_buscar = 60

# Utilizar un bucle for para buscar el número
for numero in numeros:
    if numero == numero_buscar:
        print(f"¡Número encontrado! {numero} está en la lista.")
        break
else:
    print(f"{numero_buscar} no se encontró en la lista.")

#Ejercicio 8

while True:
    print("Menú de opciones:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("0. Salir")

    opcion = input("Seleccione una opción (1/2/3/0): ")

    if opcion == "1":
        print("Ha elegido la Opción 1.")
    elif opcion == "2":
        print("Ha elegido la Opción 2.")
    elif opcion == "3":
        print("Ha elegido la Opción 3.")
    elif opcion == "0":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida (1/2/3/0).")
