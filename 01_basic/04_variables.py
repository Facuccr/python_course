##
# 04 - Variables
# Las variables sirven para guardar datos en memoria.
# Python es un lenguaje de tipado dinámico y de tipado fuerte.
###

my_name = "Facundo"
age = 19

print(my_name)

# Las variables pueden reasignarse.

#### Tipado DINAMICO: el tipo de dato se deternima en tiempo de ejecucion.
name = "facu"
print(type(name))

name = 39
print(type(name))

#### Tipado Fuerte: Pyrhon no realiza conversiones de tipo automatico.
# print(10 + "2") #### NO

## f-string (literal de cadena de formato)
print(f"Hola {my_name}, tengo {19} años ")


# asignacion no recomendada de variables.
name, age, city = "Facundo", 19, "Formosa"

# Convenciones de nombres de variables
mi_nombre_de_variable = "bien" #snake_case RECOMENDADO

# NO existe una sintaxis para declarar constantes, 
# pero se pueden simular (igualmente pueden reasignarse)
MI_CONSTANTE = 3.14 # UPPER_CASE --> constante

## nombre no validos 
# 123123_variable = error
# mi-variable = error
# mi variable = error (obvio bobis)
# Palabras Reservadas NO


# Anotaciones de tipo (opcional, para mayor claridad en el código)
is_user_logged_in: bool = True # Indica que la variable es un booleano
print(is_user_logged_in)

name: str = "midudev" # Indica que la variable es una cadena de texto
print(name)

