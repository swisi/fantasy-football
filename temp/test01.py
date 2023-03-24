import pandas as pd
import nfl_data_py as nfl


years = [2022]  # Change this to use other years if needed
columns_R = ['player_id', 'position', 'team', 'player_name', 'jersey_number', 'status']
     
dfp = nfl.import_rosters(years, columns_R)

print(dfp)