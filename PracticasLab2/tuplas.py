print('Ejemplo con tuplas \n\n')

# Definición de una tupla
tupla_information = ('Ana Picapiedra', 22, 95.5)
print(f'Información de la tupla: {tupla_information}')

# Desestructuración o unpacking
full_name, age, salary = tupla_information
print(f'Nombre: {full_name}, Age: {age}, Salary: {salary}')

print('\n\nImpresión de la tupla con un ciclo FOR \n')
# Impresión de los elementos de una tupla
for item in tupla_information:
    print(item)