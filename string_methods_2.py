# Otros métodos
message = 'Los cuervos de la UTVT'

# len
size = len(message)

# replace
new_message = message.replace(' _old_', ' _new_ ')

# find
indexOf = message.find('U')

# split
message_sliced = message.split()

print(f'Longitud de la cadena: {size}')
print(f'Nueva cadena: {new_message}')
print(f'Posición del elemento buscado: {indexOf}')
print(f'Cadena particionada: {message_sliced}')

