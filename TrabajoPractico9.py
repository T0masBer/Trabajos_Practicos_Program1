# Ejercicio 1

class Persona:
    def __init__(self, nombre="", edad=None, dni=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    # Setters y getters con validación
    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            print("Error: El nombre debe ser una cadena de caracteres.")

    def get_nombre(self):
        return self.__nombre

    def set_edad(self, edad):
        if isinstance(edad, int) and 0 < edad < 150:
            self.__edad = edad
        else:
            print("Error: La edad debe ser un número entero válido.")

    def get_edad(self):
        return self.__edad

    def set_dni(self, dni):
        if isinstance(dni, str) and len(dni) == 9:
            self.__dni = dni
        else:
            print("Error: El DNI debe ser una cadena de 9 caracteres.")

    def get_dni(self):
        return self.__dni

    def mostrar(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Edad: {self.__edad}")
        print(f"DNI: {self.__dni}")

    def es_mayor_de_edad(self):
        return self.__edad >= 18


# Ejemplo de uso
persona1 = Persona()
persona1.set_nombre("Juan")
persona1.set_edad(25)
persona1.set_dni("123456789")

persona1.mostrar()

if persona1.es_mayor_de_edad():
    print("Es mayor de edad.")
else:
    print("No es mayor de edad.")


# Ejercicio 2

class Cuenta:
    def __init__(self, titular=None, cantidad=0.0):
        self.__titular = titular
        self.__cantidad = cantidad

    # Setters y getters
    def set_titular(self, titular):
        if isinstance(titular, Persona):
            self.__titular = titular
        else:
            print("Error: El titular debe ser una instancia de la clase Persona.")

    def get_titular(self):
        return self.__titular

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def get_cantidad(self):
        return self.__cantidad

    def mostrar(self):
        print("Datos de la cuenta:")
        self.__titular.mostrar()
        print(f"Cantidad: {self.__cantidad}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
            print(f"Se ha ingresado {cantidad} a la cuenta.")
        else:
            print("Error: La cantidad a ingresar debe ser un número positivo.")

    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad
            print(f"Se ha retirado {cantidad} de la cuenta.")
        else:
            print("Error: La cantidad a retirar debe ser un número positivo.")


# Ejemplo de uso
persona_titular = Persona("Juan", 30, "123456789")
cuenta1 = Cuenta(persona_titular, 1000.0)

cuenta1.mostrar()

cuenta1.ingresar(500.0)
cuenta1.retirar(200.0)

cuenta1.mostrar()

# Ejercicio 3


class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def imprimir_lado_mayor(self):
        lado_mayor = max(self.lado1, self.lado2, self.lado3)
        print(f"El lado con tamaño mayor es: {lado_mayor}")

    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"


# Función para ingresar un número validado
def ingresar_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            if numero > 0:
                return numero
            else:
                print("Error: Ingrese un número positivo.")
        except ValueError:
            print("Error: Ingrese un número válido.")


# Programa principal
lado1 = ingresar_numero("Ingrese el primer lado del triángulo: ")
lado2 = ingresar_numero("Ingrese el segundo lado del triángulo: ")
lado3 = ingresar_numero("Ingrese el tercer lado del triángulo: ")

triangulo = Triangulo(lado1, lado2, lado3)

triangulo.imprimir_lado_mayor()
print(f"El triángulo es de tipo: {triangulo.tipo_triangulo()}")


# Ejercicio 4

class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}"


class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self):
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        email = input("Ingrese el email del contacto: ")
        nuevo_contacto = Contacto(nombre, telefono, email)
        self.contactos.append(nuevo_contacto)
        print("Contacto agregado con éxito.")

    def listar_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            for contacto in self.contactos:
                print(contacto)

    def buscar_contacto(self):
        nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre_buscar.lower():
                print(contacto)
                return
        print(f"No se encontró un contacto con el nombre {nombre_buscar}.")

    def editar_contacto(self):
        nombre_editar = input("Ingrese el nombre del contacto a editar: ")
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre_editar.lower():
                nuevo_telefono = input(
                    "Ingrese el nuevo teléfono del contacto: ")
                nuevo_email = input("Ingrese el nuevo email del contacto: ")
                contacto.telefono = nuevo_telefono
                contacto.email = nuevo_email
                print("Contacto editado con éxito.")
                return
        print(f"No se encontró un contacto con el nombre {nombre_editar}.")

    def menu(self):
        while True:
            print("\n=== Menú de Agenda ===")
            print("1. Añadir contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")

            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == "1":
                self.agregar_contacto()
            elif opcion == "2":
                self.listar_contactos()
            elif opcion == "3":
                self.buscar_contacto()
            elif opcion == "4":
                self.editar_contacto()
            elif opcion == "5":
                print("Agenda cerrada. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Ingrese un número del 1 al 5.")


# Ejemplo de uso
agenda_personal = Agenda()
agenda_personal.menu()
