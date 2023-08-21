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











