import pandas as pd

nba_players_name = pd.read_csv('D:\\DataFiles\\nba_players_a.csv', sep=',', usecols=['Name']).squeeze()
nba_players_age = pd.read_csv('D:\\DataFiles\\nba_players_a.csv', sep=',', usecols=['AGE']).squeeze()

print(f'Nombre de los jugadores: \n{nba_players_name}')
print(f'Edad de los jugadores: \n{nba_players_age}')

print(f'Funcion LEN : {len(nba_players_name)}')
print(f'Función TYPE : {type(nba_players_name)}')
print(f'Función SORTED : {sorted(nba_players_age)}')
print(f'Función Max : {max(nba_players_age)}')
print(f'Función MIN : {min(nba_players_age)}')