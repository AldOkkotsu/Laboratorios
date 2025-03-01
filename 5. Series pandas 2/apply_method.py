import pandas as pd

def convert_upper(value):
    return value.upper()
nba_players_name = pd.read_csv('D:\\DataFiles\\nba_players_a.csv',sep=',', usecols= ['Name']).squeeze()
result = nba_players_name.apply(convert_upper).head()

print(result)