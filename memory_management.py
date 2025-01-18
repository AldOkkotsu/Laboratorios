# Variables
number_x = 10
number_y = 20

# Obtener las direcciones de memoria
address_id_x = id(number_x)
address_id_y = id(number_y)

print("*** Antes de actualizar la variable X ***")
print(address_id_x)
print(address_id_y)

number_x = 15
address_id_x = id(number_x)

print("*** Después de actualizar la variable X ***")
print(address_id_x)
print(address_id_y)