import pandas as pd

nba_players = pd.read_csv('D:\\DataFiles\\nba_players_a.csv', sep=',', usecols=['Name']).squeeze()

#Función describe
print(f'Función describe con una serie  : {nba_players.describe()}')

#Función head
print(f'Primeros 5 elementos de una serie:\n {nba_players.head()}')

print(f'\n\n Primeros 10 elementos de una serie:\n {nba_players.head(10)}')

#Función tail
print(f'\n\n\nPrimeros 5 elementos de una serie:\n {nba_players.tail()}')
print(f'\n\n\n Primeros 10 elementos de una serie:\n {nba_players.tail(10)}')