#Ejercico1

base=float(input())
altura=float(input())

perimetro= base*altura

#Ejercicio2

cat1=float(input())
cat2=float(input())

hip= (cat1**2 + cat2**2)**1/2

#Ejercicio3

num1=int(input())
num2=int(input())

suma= num1+num2
print(suma)

resta= num1-num2
print(resta)

multiplicacion= num1*num2
print(multiplicacion)

division= num1/num2
print(division)

#Ejercicio4

fahr=(float(input('Ingrese los grados en Fahrinheti para convertilos a Celsius')))

cels= (fahr-32)*5/9
print(fahr,' grados fahreinheit son',cels,' grados Celsius')

#Ejercicio5

#a)Hay una variable dentro del input que no esta definida y en todo caso es innecesaria, yo lo pondria de la sig forma:
nombre_cancion= input('Cual es tu cancion favorita?')

"""b)Al momento de ingresar un valor con input este se toma como un string si antes no se lo define como int o float,
 por lo que daria error al intentar hacer la cuenta, la forma correcta de hacerlo seria:"""
 
precio=float(input('Precio: '))
total= precio+(precio*0.10)

#c)En la instruccion print(tu edad es) no tiene puestas comillas por lo que daria error al ejecutarse, lo correcto seria:

edad = int(input('Edad: '))
print('tu edad es', edad)

"""d)La instruccion da a entender que se quiere comprobar si uno tiene 18
pero lo que se hace es cambiar el valor de la variable a 18 sin comprobar nada
para comprobar si tiene 18 haria lo sig:"""

print('Veamos si tu edad es 18')
edad=int(input('Edad:'))

if edad==18:
    print('Tienes 18 yay!')
else:
    print('No tienes 18 :(')

#Ejercicio6

print('Ingrese 3 numeros para calcualr su media')
num1= int(input())
num2= int(input())
num3= int(input())

media= (num1+num2+num3)/3
print('La media es:',media)

#Ejercicio7

def conversion_horas_minutos(minutos):
    horas= minutos//60
    minutos_restantes= minutos % 60
    return horas,minutos_restantes

minutos_pedidos=int(input('Ingrese los minutos que quiera convertir en horas y minutos: '))

horas_resultado, minutos_resultado= conversion_horas_minutos(minutos_pedidos)

print(f"{minutos_pedidos} minutos corresponden a {horas_resultado} horas y {minutos_resultado} minutos")

#Ejercicio8

comision= 0.10

sueldo_base=float(input('Ingrese el sueldo base del empleado'))
cantidad_comisiones=int(input('Ingrese el numero de ventas realizadas por el empleado'))

comision_total= sueldo_base*(cantidad_comisiones*comision)
sueldo_total= sueldo_base + comision_total

print(f'El empleado gana {comision_total} por comision de ventas, dejando su sueldo total en: {sueldo_total}')

#Ejercicio9

descuento= 0.15

total_compra=float(input('Ingrese el total de la compra'))
precio_final= total_compra-(total_compra*descuento)
print('El precio final a pagar es de: ',precio_final)

#Ejercicio10

def calcular_calificacion_final(calificaciones_parciales, calificacion_examen_final, calificacion_trabajo_final):
    promedio_parciales = sum(calificaciones_parciales) / len(calificaciones_parciales)
    calificacion_final = 0.55 * promedio_parciales + 0.30 * calificacion_examen_final + 0.15 * calificacion_trabajo_final
    return calificacion_final

try:
    calificaciones_parciales = []
    for i in range(3):
        calificacion_parcial = float(input(f"Ingrese la calificación del parcial {i + 1}: "))
        calificaciones_parciales.append(calificacion_parcial)
    
    calificacion_examen_final = float(input("Ingrese la calificación del examen final: "))
    calificacion_trabajo_final = float(input("Ingrese la calificación del trabajo final: "))
    
    calificacion_final = calcular_calificacion_final(calificaciones_parciales, calificacion_examen_final, calificacion_trabajo_final)
    print(f"La calificación final del alumno en la materia de Algoritmos es: {calificacion_final:.2f}")
except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")

#Ejercicio11

print('Ingrese 2 numeros para saber la distancia entre ellos')
num1=int(input())
num2=int(input())
distancia_entre_nums=abs(num1-num2)
print('La distancia entre ambos numeros es: ',distancia_entre_nums)

#Ejercicio12

num=float(input('Ingrese un numero'))
raiz_cuadrada= num**1/2
raiz_cubica= num**1/3
print('Raiz cuadrada del numero: ',raiz_cuadrada)
print('Raiz cubica del numero: ',raiz_cubica)

#Ejercicio13

print('Ingrese un numero de 2 cifras')
numero=int(input)
cifra1= numero//10
cifra2= numero%10
numero_invertido= cifra2*10 + cifra1
print(f'El numero invertido es: {numero_invertido}')

#Ejercicio14

print("Ingrese 2 valores")
varA=input()
varB=input()

aux=varA
varA=varB
varB=aux
print(varA,varB)

#Ejercicio15

HH = int(input("Ingrese la hora de partida (HH): "))
MM = int(input("Ingrese los minutos de partida (MM): "))
SS = int(input("Ingrese los segundos de partida (SS): "))
T = int(input("Ingrese el tiempo de viaje en segundos (T): "))

tiempo_partida = HH * 3600 + MM * 60 + SS

# Calcular el tiempo total en segundos
tiempo_total = tiempo_partida + T

nuevas_horas = tiempo_total // 3600
nuevos_minutos = (tiempo_total % 3600) // 60
nuevos_segundos = tiempo_total % 60

print(f"Hora de llegada a la ciudad B: {nuevas_horas:02d}:{nuevos_minutos:02d}:{nuevos_segundos:02d}")

#Ejercicio16

print('Ingrese su:')
nombre=input('Nombre: ')
apellido1=input('Primer apellido: ')
apellido2=input('Segundo apellido: ')

print(f'Sus inciales son: {nombre.upper(0)}.{apellido1.upper(0)}.{apellido2.upper(0)}')

#Ejercicio17

usuario=input("Ingresa tu nombre")
print(f'Ahora estas en la matrix{usuario}')

#Ejercicio18

valor_cena=int(input('Cuanto costo tu cena?'))
concepto_servicio= valor_cena*0.062
propina=valor_cena*0.10
total_pagar=valor_cena+concepto_servicio+propina

print(f'El total a pagar de la cena sumando el servicio y propina es de: {total_pagar}')

#Ejercicio19

print('Ingrese su fecha de nacimiento')
dia=input('Dia')
mes=input('Mes')
anio=input('Año')

print(f'Naciste el {dia}/{mes}/{anio}')

#Ejercicio20

fecha_str = input("Ingrese su fecha de nacimiento en formato DDMMAAAA: ")

fecha_dict = {
    "dia": int(fecha_str[0:2]),
    "mes": int(fecha_str[2:4]),
    "anio": int(fecha_str[4:8])
}

print(f"Su fecha de nacimiento es: {fecha_dict['dia']:02d}/{fecha_dict['mes']:02d}/{fecha_dict['anio']:04d}")

#Ejercicio21

def calcular_tanques_combustible(km_por_litro, capacidad_tanque, km_totales):
    km_por_tanque = km_por_litro * capacidad_tanque
    tanques_necesarios = km_totales / km_por_tanque
    return tanques_necesarios

try:
    km_por_litro = float(input("Ingrese cuántos kilómetros puede recorrer su moto con 1 litro de combustible: "))
    capacidad_tanque = float(input("Ingrese la capacidad del tanque en litros: "))
    km_totales = float(input("Ingrese cuántos kilómetros recorrerán en total: "))
    
    tanques_necesarios = calcular_tanques_combustible(km_por_litro, capacidad_tanque, km_totales)
    print(f"Para el viaje de {km_totales:.2f} kilómetros, se necesitarán {tanques_necesarios:.2f} tanques de combustible.")
except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")








