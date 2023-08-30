#Ejercicio 1

print('Cuantos anios tiene su computadora?')
anios_pc=int(input())

if anios_pc <= 2:
    print('La computadora es nueva')

elif anios_pc >= 2:
    print('La computadora es vieja')

#Ejercicio 2

print('Cuantos anios tiene su computadora?')
anios_pc=int(input())

if anios_pc <= 2:
    print('La computadora es nueva')

elif anios_pc >= 2:
    print('La computadora es vieja')

elif anios_pc < 0:
    print('Error, el numero es negativo')


#Ejercicio 3

nombre1=input('Ingrese el primer nombre')
nombre2=input('Ingrese el segundo nombre')

if nombre1(0) == nombre2(0):
    print('Coincidencia!')
else:
    print('No hay coincidencia')

#Ejercicio 4

print('Eleccion de candidato')
print('Candidato A del partido rojo')
print('Candidato B del partido verdad')
print('Candidato C del partido azul')

opcion=input('Elija su candidato A/B/C').upper()

if opcion == 'A':
    print('Ha votado por el partido rojo')

elif opcion == 'B':
    print('Ha votado por el partido verdad')

elif opcion == 'C':
    print('Ha votado por el partido azul')

else: 
    print('Opcion incorrecta')

#Ejercicio 5

letra=input('Ingrese una letra')

if len(letra) == 1:
    letra.lower()
else:
    print('No se puede procesar el dato ingresado')

if letra in ['a','e','i','o','u']:
    print('La letra ingresada es vocal')
else:
    print('La letra ingresada no es vocal')

#Ejercicio 6

anio=int(input('Ingrese el anio para saber si es bisiesto'))

if anio%4 or anio%400 and anio%100 !=0 :
    print('El anio ingresado es bisiesto')
else:
    print('El anio ingresado no es bisiesto')

#Ejercicio 7

print('Ingrese tres numeros')
num1=int(input('Numero 1'))
num2=int(input('Numero 2'))
num3=int(input('Numero 3'))

menor=min(num1,num2,num3)

print(f'El numero menor es: {menor}')

#Ejercicio 8

print('Ingrese su usuario y Contraseña')
usuario=input('Usuario')
contrasenia=input('Contraseña')

if usuario == 'Genevere' and contrasenia == 'excalibur':
    print('Usuario y contraseña correctos, puede ingresar a Camelot')
else:
    print('Acceso denegado')

#Ejercicio 9

nombre = input("Ingresa tu nombre: ")
sexo = input("Ingresa tu sexo (H para hombre, M para mujer): ")

nombre = nombre.upper()

if (sexo == "M" and nombre < "M") or (sexo == "H" and nombre >= "N"):
    grupo = "A"
else:
    grupo = "B"

print(f"Tu grupo es el grupo {grupo}")

#Ejercicio 10

print('Ingrese su edad porfavor')

edad=int(input())

if edad <= 4:
    print('Su entrada es gratis')
elif  edad > 4 and edad < 18:
    print('El valor de su entrada es de: $500')
elif edad >= 18:
    print('El valor de su entrada es de: $1000')

#Ejercicio 11

print('Que tipo de pizza desea?(V para vegetariana, NV para no vegetariana)')

pizza=input()

if pizza == 'V':
    print("Los ingredientes disponibles para pizza vegetaria son: Pimiento y Tofu(solo puede elegir uno)")
    ingrediente=input('Ingrese el ingrediente que desea')
    ingrediente.lower
elif pizza== 'NV':
    print('Los ingredientes para pizza no vegetariana son: Pepperoni, Jamon y Salmon(solo puede elegir uno)')
    ingrediente=input('Ingrese el ingrediente que desea')
    ingrediente.lower
else:
    print('Opcion no valida')

if ingrediente == 'pimiento' or ingrediente == 'tofu':
    print(f'Su pizza es vegetariana, sus ingredienres son: mozzarela, tomate y {ingrediente}')
elif ingrediente == 'pepperoni' or ingrediente == 'jamon' or ingrediente == 'salmon':
    print(f'Su pizza no es vegetariana, sus ingredientes son: mozzarela, tomate y {ingrediente}')

#Ejercicio 12

actual=int(input('Ingrese el año actual'))
cualquiera=int(input('Ingrese cualquier otro año'))

resultado= actual-cualquiera

if resultado > 0:
    print(f'Han pasado {resultado} desde el año {cualquiera}')
elif resultado < 0:
    print(f'Faltan {abs(resultado)} años para el año {cualquiera}')
elif resultado == 0:
    print('Es el año actual')

#Ejercicio 13

num1=int(input('Ingresa el primero numero'))
num2=int(input('Ingresa el segundo numero'))

if num1 <= 0 or num2 <= 0:
    print('Por favor ingrese numeros enteros positivos')
else:
    mayor= max(num1,num2)
    menor= min(num1,num2)

if mayor % menor == 0:
    print(f'{mayor} es multiplo de {menor}')
else:
    print(f'{mayor} no es multiplo de {menor}')

#Ejercicio 14

a=float(input('Ingresa el coeficiente "a": '))
b=float(input('Ingresa el coeficiente "b": '))

if a == 0 and b == 0:
    print('Todos los numeros son solucion')

elif a == 0:
    print('La ecuacion no tiene solucion')

else:
    
    x= -b/a
    print(f'La solucion de la ecuacion es: {x}')

#Ejercicio 15

print('El area de que figura desea calcular, circulo o triangulo?')

opcion=input('Escriba C para circulo o t para triangulo')
opcion.lower

if opcion == 't':
    print('Ingrese los valores de la altura y base del triangulo')
    altura=float(input('Altura: '))
    base=float(input('Base: '))

    area= (base*altura)/2
    print(f'El area del triangulo es: {area}')

elif opcion == 'c':
    print('Ingrese el radio del circulo')
    radio=float(input('Radio: '))

    area= 3.14 * radio**2
    print(f'El area del circulo es: {area}')

else:
    print('Ingrese una opcion valida')
    

#Ejercico 16

print('Ingrese dos valores de los que desee realizar una operacion')
a=float(input('Valor1'))
b=float(input('Valor2'))

print('Que operacion quiere realizar?')
operacion=int(input('Suma(1),Multiplicacion(2),Resta(3),Division(4)'))

if operacion == 1:
    suma=a+b
    print(f"El resultado es: {suma}")
elif operacion == 2:
    mult=a*b
    print(f"El resultado es: {mult}")
elif operacion == 3:
    resta=a-b
    print(f'El resultado es: {resta}')
elif operacion == 4:
    div=a/b
    print(f'El resultado es: {div}')
else:
    print('Ingrese una opcion valida')


#Ejercicio 17

dia=input('Ingresa el dia de la semana')
dia.lower

if dia == 'lunes':
    print('Recien empezando la semana pa')
elif dia == 'viernes':
    print('Vamos que se termina')
elif dia == 'sabado' or dia == 'domingo':
    print('Ya estamos en el finde!!')
else:
    print('Todavia falta para terminar')

#Ejercico 18

hs_mes=int(input('Cuantas horas trabajo en el mes?'))
salario_hora=int(input('Cual es su salario por hora?'))

if hs_mes == 48:
    sueldo_final= hs_mes*salario_hora
    print(f'Su pago de este mes es de ${sueldo_final}')
elif hs_mes > 48:
    horas_extra= hs_mes - 48
    sal_hs_extra= horas_extra * (salario_hora * 1.10)
    sal_normal= 48 * salario_hora
    sueldo_final= sal_hs_extra + sal_normal
    print(f'Su pago de este mes es de ${sueldo_final}')
else:
    print('Ingrese las horas correctamente')

#Ejercicio 19

precio_lapiz=60

cantidad_lapiz=int(input('Cuantos lapices esta comprando?'))

if cantidad_lapiz >= 1000:
    precio_total= cantidad_lapiz*precio_lapiz
    descuento= precio_total*0.07
    precio_final= precio_total-descuento
    print(f'El total a pagar es de ${precio_final}')
else:
    precio_final= cantidad_lapiz*precio_lapiz
    print(f'El total a pagar es de ${precio_final}')

#Ejercicio 20

print('Ingresa tus 4 notas')
nota1=float(input())
nota2=float(input())
nota3=float(input())
nota4=float(input())

promedio= (nota1+nota2+nota3+nota4)/4

if promedio >= 6:
    print('Alumno aprobado')
else:
    print('Alumno desaprobado')




