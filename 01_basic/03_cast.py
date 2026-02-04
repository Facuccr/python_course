###
# 03 - casting de types
# Transformar un tipo de un valor a otro 
###

print("conversion de tipos:")

print(type(int("100")))

print(int("100") + 2)
print("100" + str(2))

print(type(float("3.1416")))

print(bool(3)) # True
print(bool(0)) # False
## el unico numero que se transforma en False en 
# es el 0

print(bool("")) # False
print(bool(" ")) # True
print(bool("False")) # True