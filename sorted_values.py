import pandas as pd

nba_players = pd.read_csv('D:\\DataFiles\\nba_players_a.csv', usecols= ['Name']).squeeze()

result_from_a = nba_players.sort_values()
result_from_z = nba_players.sort_values(ascending=False)

print(f'De la letra A a la letra Z : {result_from_a}')
print(f'De la letra Z a la letra A : {result_from_z}')