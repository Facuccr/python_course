###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###

from os import system
if system("clear") != 0: system("cls")


print("Sentencia simple condicional:")

edad = 18

if edad >= 18:
    print("eres mayor de edad") 


print("Sentencia condicional  con else:")

edad = 15

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("eres menor de edad")


print("Sentencia condicional con ELIF:")

nota = 7
if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 6:
    print("Aprobado")
else:
    print("No estas calificado")


print ("Condicionales multiples")

# && -> and
# || -> or
# ! -> not

edad = 18
tiene_carnet= False

if edad >=18 and  tiene_carnet:  
    print("Puede conducir")
else:
    print("No puede conducir")


es_fin_de_semana = True

if not es_fin_de_semana:
    print("no es fin de semana")


print("anidar condicionales")

edad = 18
tiene_dinero = True
if edad >= 18:
    if tiene_dinero:
        print("Podes entrar a la discoteca")
    else:
        print("no podes entrar")
else:
    print("no podes entrar")

# simplificado:
# if edad < 18:
#     print("no podes entrar")
# elif tiene_dinero:
#     print("podes entrar")
# else:
#     print("quedate noma en tu casa")

numero = 5 # True
if numero:
    print("el numero no es cero")

numero = 0 # False
if numero:
    print("no entrara nunca aca")

numero = "" # False
if numero:
    print("el nombre es vacio por lo que no entra")


numero = 3 # asignacion =
es_el_tres = numero == 3 # comparacions

if es_el_tres:
    print("definitivamente es el tres")


# A veces podemos crear condicionales en una sola línea usando
# las ternarias, es una forma concisa de un if-else en una línea de código
print("\nLa condición ternaria:")
# [código si cumple la condición] if [condicion] else [codigo si no cumple]

edad =16
mensaje = "es mayor de edad" if edad >= 18 else "es menor de edad"
print(mensaje)

###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# numero_1 = input("ingrese el primer numero:")
# numero_2 = input("ingrese el segundo numero:")


# if numero_1 > numero_2:
#     print(f"{numero_1} es mayor que {numero_2}")
# elif numero_2 > numero_1:
#     print(f"{numero_2} es mayor que {numero_1}")
# else:
#     print("los numeros son iguales")
 

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# num_1 = float(input("ingrese primer numero: "))
# num_2 = float(input("ingrese segundo numero: "))
# operacion = input("Ingrese la operacion a realizar: ")

# if operacion == "+":
#     resultado = num_1 + num_2
# elif operacion == "-":
#     resultado = num_1 - num_2
# elif operacion == "*":
#     resultado = num_1 * num_2
# elif operacion == "/":
#     if num_2 == 0:
#         print("Error: no es posible dividir por 0")
#     else:
#         resultado = num_1 / num_2
# else:
#     print("La operacion no puede realizarse")

# # ! la propiedad locals comprueba si la variable resultado existe.
# if 'resultado' in locals():
#     print(f"El resultado de la operacion es {resultado}")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# anio = int(input("Introduce un año: "))

# if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
#     print(f"{anio} es un año bisiesto.")
# else:
#     print(f"{anio} no es un año bisiesto.")


# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

edad = int(input("introduzca una edad"))

if 0 <= edad <= 2:
    print("Bebé")
elif 3 <= edad <= 12:
    print("Niño")
elif 13 <= edad <= 17:
    print("Adolescente")
elif 18 <= edad <= 64:
    print("Adulto")
elif edad >= 65:
    print("Adulto mayor")
else:
    print("Edad no válida.")