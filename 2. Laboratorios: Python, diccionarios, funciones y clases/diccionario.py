# Declarar un diccionario en Python

student = {
    'name': 'Fokin yo',
    'age': 25,
    'language': 'Python',
    'city': 'Lerna'
}

# Acceso a los valores de un diccionario
print(f'Contenido total del estudiante: {student}')
print(f'Nombre: {student["name"]}')
print(f'Edad: {student.get("age")}')

print('--- Operaciones Básicas sobre diccionarios ---')
# Modificar los valores de un diccionario
student['language'] = 'C#'
print(f'\nContenido actual del estudiante una vez modificado el lenguaje: {student}')

# Eliminar un elemento de un diccionario

student.pop('city')
print(f'\nContenido del estudiante una vez eliminada la ciudad: {student}')

# Agregar un nuevo elemento
student['food'] = 'Galletas'
print(f'Contenido del estudiante una vez agregada una nueva propiedad: {student}')

print('\n\n\n--- Iterar sobre un diccionario ---')
print('\nIteracion de los elementos de un diccionario, simple')

for element in student:
    print(f'{element}: {student[element]}')


print('\nIteracion de los elementos de un diccionario, destructuración - unpacking ')

for key, value in student.items():
    print(f'Llave: {key}, Valor: {value}')

print('\n\nIteración de los elementos de un diccionario, llaves ')

for key in student.keys():
    print(f'Llave: {key}')

print('\n\nIteración de los elementos de uin diccionario, valores ')

for value in student.values():
    print(f'Valor: {value}')
