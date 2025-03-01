import pandas as pd

nba_players = pd.read_csv('D:\\DataFiles\\nba_players_a.csv', usecols= ['Name']).squeeze()

single_value = nba_players.iloc[99]
print(single_value)

multi_value = nba_players.iloc[:100].tolist()
multi_value_2 = nba_players.iloc[:100]
print(multi_value)
print(len(multi_value))

print(type(multi_value))
print(type(multi_value_2))