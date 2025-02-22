import pandas as pd

kid_gifts = {
    'VideoGames' : 'Play 5',
    'BoardGames' : 'Monopoly',
}

serie = pd.Series(kid_gifts)

print(f'\n{serie}')