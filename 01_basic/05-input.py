###
# 05 - Entrada de usuario (input()) - Versión simplificada
# La función input() permite obtener datos del usuario a través de la consola.
###

nombre = input("Hola, como te llamas? \n" )
print(f"Hola {nombre} encantado de conocerte")

# La función input() devuelve un string asi
# que si queremos obtener un número se debe convertir el string a un número
age = input("¿Cuántos años tienes?\n")
age = int(age)
print(f"Tienes {age} años")

print("obtener multiples variables a la vez:")
country, city = input("en que pais y ciudad vives?\n").split()

print(f"Vives en {country}, {city}")
