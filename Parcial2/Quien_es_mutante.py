from FuncionesP import *

while True:
    print('A continuacion se le pedira ingresar una secuencia de ADN para saber si es mutante')
    main()
    try:
        aux = int(input(
            'Si desea salir ingrese 0, para continuar ingrese cualquier otro numero: '))
        if aux == 0:
            break  # Salir del bucle si el usuario ingresa 0
    except ValueError:
        print('Entrada no válida. Por favor, ingrese 0 para salir o cualquier otro número para continuar.')
