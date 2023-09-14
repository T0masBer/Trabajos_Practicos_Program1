#Ejercicio 1
word=input("Ingrese una palabra\n")
counter=10
while counter>0:
    counter-=1
    print(word)
#Ejercicio 2
age=int(input("Ingrese su edad\n"))
if type(age) != int:
    print("ERROR, el valor ingresado no es numerico")
elif age<0:
    print("El valor ingresado es menor a 0")
else:
    for z in range(age):
        print(f"Usted ha cumplido {z+1} año/s")
#Ejercicio 3
number=int(input("Ingrese un numero entero positivo\n"))
oddlist=[]
if number<0:
    print("ERROR, el valor ingresado es negativo")
else:
    z=1
    while z<number:
        z+=1
        if z % 2 != 0:
            oddlist.append(str(z))
print("Todos los impares despues del 1:\n", ", ".join(oddlist))
#Ejercicio 4
number=int(input("Ingrese un numero entero positivo\n"))
backnumbers=[]
while number>0:
    number-=1
    backnumbers.append(str(number))
print("Todos los numeros anteriores al ingresado son:\n", ", ".join(backnumbers))
#Ejercicio 5
investment=int(input("Ingrese el valor a invertir\n"))
interestrate=float(input("Ingrese el interes anual\n"))
investmentyears=int(input("Ingrese cuantos años va a devengar\n"))
counter=0
totalbenefit=0
while counter<=investmentyears:
    counter+=1
    totalbenefit+=(investment*(interestrate/100))
    print(f"El año {counter} devengo ${totalbenefit}")
#Ejercicio 6
number=int(input("Ingrese un numero entero positivo\n"))
slash="*"
if number>0:
    for z in range(number):
        print(slash)
        slash+="*"
#Ejercicio 7
choice=input("Quiere ver las tablas de multiplicar del 1 al 10?\n")
if choice.lower()=="si":
    for z in range(1, 11):
        print()
        for y in range(1, 11):
            print(f"{z}x{y}={z*y}")
else:
    print("Programa terminado")
#Ejercicio 8
number=int(input("Ingrese un número entero\n"))
for z in range(1, number+2):
    for x in range(z, 1, -1):
        print(x - 1, end='')
    print()
#Ejercicio 9
counter=1
while counter!=0:
    password=input("Ingrese la contraseña\n")
    if password.lower()=="contraseña":
        counter=0
        print("Contraseña correcta")
        break
    print("Contraseña incorrecta")
#Ejercicio 10
prime=int(input("Ingrese un numero para saber si es numero primo\n"))
divisiblecounter=0
for z in range(prime+1, 0, -1):
    if prime % z == 0:
        divisiblecounter+=1
if divisiblecounter>2:
    print("No es primo")
else:
    print("Es primo")
#Ejercicio 11
word=input("Ingrese una palabra\n")
for z in range(len(word), 0, -1):
    letter=word[z-1]
    print(letter)
#Ejercicio 12
phrase=input("Ingrese una frase\n")
letter=input("Ingrese la letra que desea buscar en la frase ingresada\n")
lettercount=0
for z in phrase:
    if z.lower()==letter.lower():
        lettercount+=1
print(f"La cantidad de veces que la letra aparece en la frase es {lettercount}")
#Ejercicio 13
inout="entrar"
while inout.lower()!="salir":
    inout=input("Ingrese cualquier cosa\n")
    if inout.lower()!="salir":
        print(f"<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<{inout}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#Ejercicio 14
firstnumber=int(input("Ingrese el primer numero\n"))
secondnumber=int(input("Ingrese el segundo numero\n"))
for z in range(firstnumber, secondnumber, 1):
    if z % 2 == 0:
        print(f"{z} (Par)", end=" ")
    if z % 2 != 0:
        print(f"{z} (Impar)", end=" ")
#Ejercicio 15
number=int(input("Ingrese un numero entero mayor que cero\n"))
for z in range(number, 0, -1):
    if number % z == 0:
        print(f"{z} es divisor de {number}")
else:
    print("El numero ingresado no es un entero mayor que cero")
#Ejercicio 16
numbers=int(input("Cuantos numeros va a ingresar?\n"))
negativenumbers=0
for z in range(numbers):
    number=int(input(f"Ingrese el numero de la posicion {z}\n"))
    if number<0:
        negativenumbers+=1
print(f"Los numeros negativos ingresados fueron {negativenumbers}")
#Ejercicio 17
phrase=input("Ingrese una frase\n")
vowels=["a", "e", "i", "o", "u"]
whatvowels=[]
acounter=0
ecounter=0
icounter=0
ocounter=0
ucounter=0
for z in phrase:
    if z in vowels:
        if z==vowels[0] and acounter<1:
            acounter+=1
            whatvowels.append(vowels[0])
        if z==vowels[1] and ecounter<1:
            ecounter+=1
            whatvowels.append(vowels[1])
        if z==vowels[2] and icounter<1:
            icounter+=1
            whatvowels.append(vowels[2])
        if z==vowels[3] and ocounter<1:
            ocounter+=1
            whatvowels.append(vowels[3])
        if z==vowels[4] and ucounter<1:
            ucounter+=1
            whatvowels.append(vowels[4])
print(f"Las vocales que aparecen en la frase son: {', '.join(whatvowels)}")
#Ejercicio 18
number=int(input("Ingrese un numero entero\n"))
one=0
two=1
next=two
print(one, end=" ")
print(next, end=" ")
for z in range(number):
    print(next, end=" ")
    one=two
    two=next
    next=one+two
#Ejercicio 19
savingscan=int(input("Ingrese la cantidad a ahorrar\n"))
savings=0
while savings<savingscan:
    saving=int(input("Ingrese la cantidad a guardar como ahorro en la alcancia\n"))
    if saving<1:
        print("No puede ahorar un monto negativo o nulo!")
    else:
        savings+=saving
print("La alcancia ha superado o igualado la cantidad destinada a ahorrar!")
#Ejercicio 20
number=1
sumatory=0
while number!=0:
    number=int(input("Ingrese un numero positivo\n"))
    sumatory+=number
print(f"La sumatorio final es {sumatory}")
#Ejercicio 21
number=1
largest=0
while number!=0:
    number=int(input("Ingrese un numero positivo\n"))
    if number>largest:
        largest=number
print(f"El mayor numero ingresado fue {largest}")
#Ejercicio 22
number=0
digitsumatory=0
evencounter=0
while number!=-1:
    digitsumatory=0
    number=int(input("Ingrese un numero\n"))
    if number!=-1:
        counter=0
        while counter<len(str(number)):
            digit=str(number)[counter]
            counter+=1
            digitsumatory+=int(digit)
    if number % 2 == 0:
        evencounter+=1
        print(f"La suma de todas las cifras del numero ingresado es {digitsumatory}")
print(f"La cantidad de numeros pares ingresados fue {evencounter}")
#Ejercicio 23 y 24
amount=1
totalamount=0
while amount!=0:
    amount=int(input("Ingrese el monto de su compra\n"))
    if amount>-1:
        totalamount+=amount
    else:
        print("El monto no puede ser negativo, ingrese un nuevo monto")
if totalamount>1000:
    totalamount=totalamount-(totalamount*0.10)
    print(f"El total a pagar es {totalamount}")
else:
    print(f"El total a pagar es {totalamount}")
#Ejercicio 25
number=int(input("Ingrese un numero\n"))
factorial=1
for z in range(1, number+1):
    factorial*=z
print(f"El factorial de {number} es {factorial}")
