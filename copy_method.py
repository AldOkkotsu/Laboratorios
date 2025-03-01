import pandas as pd

nba_players_df = pd.read_csv('D:\\DataFiles\\nba_players_a.csv',sep=',', usecols= ['Name']).head(5)
nba_players_copy = nba_players_df.squeeze().copy()
nba_players_view = nba_players_df.squeeze()

nba_players_copy.iloc[0] = 'Lerma'
nba_players_copy.iloc[0] = 'UTVT'

print(nba_players_df)
print(nba_players_copy)
print(nba_players_view)