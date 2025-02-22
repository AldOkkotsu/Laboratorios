import pandas as pd

# Colección de datos
list_ice_cream = ['Limon', 'Chocolate', 'Vainilla']
series = pd.Series(list_ice_cream)
print(f'Este es el contenido de la serie: \n{series}')

# Indice personalizado

index = ['a','b','c']
serie_2 = pd.Series(list_ice_cream, index)

print(f'\n\nEste es el contenido de la serie 2: \n{serie_2}')