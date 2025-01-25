print("Ejemplo del uso de colecciones tipo SET")

# Definir ejemplos con colecciones
first_collection = {1, 2, 3, 4, 5}
second_collection = {3, 4, 5, 6, 7, 8}

# Imprimir el contenido de una colección de tipo SET
print(f"Mi colección de tipo SET: {first_collection}")

# Remover un elemento de la colección REMOVE
first_collection.remove(4)
print(f"Mi colección actualizada: {first_collection}")

# Agregar un elemento a la colección ADD
first_collection.add("Hola mundo")
print(f"Mi colección actualizada, ADD: {first_collection}")

# Iteración sobre una colección con un ciclo FOR
print("\nImpresión del contenido de la colección\n")
for item in first_collection:
    print(item)

# Operaciones con colecciones
union_set = first_collection.union(second_collection)
intersection_set = first_collection.intersection(second_collection)
difference_set = first_collection.difference(second_collection)

print(f"Unión de colecciones: {union_set}")
print(f"Intersección de colecciones: {intersection_set}")
print(f"Diferencia en colecciones: {difference_set}")