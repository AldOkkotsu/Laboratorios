import pandas as pd

# Cargar los datos
nba_players = pd.read_csv('D:\\DataFiles\\nba_players_a.csv', usecols=['DRtg']).squeeze()
some_values = nba_players.iloc[:5]

# Realización de una suma
addition_1 = some_values + 10
addition_2 = some_values.add(10)

print(f'Realización de una suma')
print(some_values)
print(addition_1)
print(addition_2)

# Realización de una resta
subtract_1 = some_values - 10
subtract_2 = some_values.sub(10)

print(f'Realización de una resta')
print(subtract_1)
print(subtract_2)

# Realización de multiplicación
multiply_1 = some_values * 10
multiply_2 = some_values.mul(10)

print(f'Realización de una multiplicación')
print(multiply_1)
print(multiply_2)

# Realización de división
divide_1 = some_values / 10
divide_2 = some_values.div(10)

print(f'Realización de una división')
print(divide_1)
print(divide_2)