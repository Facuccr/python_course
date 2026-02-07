###
# 03 - Listas
# Secuencias mutables de elementos.
# Pueden contener elementos de diferentes tipos.
###
from os import system
if system("clear") != 0: system("cls")

print("\nCrear listas")
lista1 = [1 ,2 ,3 ,4 ,5] #lista de enteros
lista2 = ["Manzanas", "peras", "platanos"] # lista de cadenas de textos
lista3 = [1, " hola", 3.14, True] # lista de tipos mixtos

lista_vacia = []
lista_de_listas = [[1,2], [3,4]]
matrix = [[1, 2], [2, 3], [4, 5]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrix)

print("\n acceso a elementos por indice")
print(lista2[0]) # MANZANAS
# ? ACCEDER AL ULTIMO ELEMENTO DE LA LISTA
print(lista2[-1]) # PLATANOS

# ? ACCEDER A UN ELEMENTO DE UNA LISTA DE LISTAS
print(lista_de_listas[1][0]) # 3 

# * Slicing de listas
# "corta" una lista desde una posicion a otra [desde:hasta]
lista1 = [1 ,2 ,3 ,4 ,5]
print(lista1[1:4]) # [2, 3, 4]
print(lista1[:3]) # [1, 2 ,3]
print(lista1[3:]) # [4, 5]
print(lista1[:]) # copia la lista

# El tercer parámetro es el paso (step) [desde:hasta:PASO]
# print(lista1[DESDE:HASTA:PASO (1)]
lista1 = [1 ,2 ,3 ,4 ,5, 6, 7, 8]
print(lista1[::2])
print(lista1[::-1])

#* Modificar una lista
lista1[0] = 20
print(lista1)

#* Añadir elementos a una lista

lista1 = [1, 2 , 3]

#forma larga y menos eficiente
lista1 = lista1 + [4, 5, 6]
print(lista1)

# forma corta
lista1 += [7, 8, 9]
print(lista1)


###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]

secreto = (mensaje[7:])

print(secreto)


# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

numeros = [10, 20, 30, 40, 50]

numeros[0] = 50
numeros[-1] = 10

print(numeros)



# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]

sandwich = pan + ingredientes + pan_abajo

print(sandwich)


# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

lista = [1, 2, 3]

lista_duplicada = lista + lista

print(lista_duplicada)


# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

lista = [10, 20, 30, 40, 50]

centro = len(lista) // 2
print(lista[centro])

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]

lista = [1, 2, 3, 4, 5, 6]

mitad = len(lista) // 2

lista_invertida = lista[:mitad][::-1] + lista[mitad:]

print(lista_invertida)