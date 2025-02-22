import pandas as pd

good_student_qualities = ['Disciplinado','AutoDidacta','ProgramadorFuturo','Trabajador','Orgulloso','Perezoso','Inteligente']
serie = pd.Series(good_student_qualities)
print(serie)

# El tamaño de la serie
print(f'El tamaño de la serie es el siguiente: {serie.size}')
# La serie tiene valores duplicados
print(f'La serie tiene valores duplicador: {serie.is_unique}')
# Información de los indices
print(f'Este atributo muestra información de los indices: {serie.index}')
# Formación del almacenamiento de los valores de la serie
print(f'Información de la serie: {serie.values}')
# Información del tipo de datos que se utilizan para almacenar los valores de la serie
print(f'Tipo de datos: {type(serie.values)}')