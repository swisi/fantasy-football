# import packages
import sqlite3
import pandas as pd

import nfl_data_py as nfl# load data

conn = sqlite3.connect('nfl.db')


years = [2022]
columns_R = ['team','player_name','jersey_number','status']

dfp = nfl.import_rosters(years,columns_R)
dft = nfl.import_team_desc()

dft.drop(dft.columns[[6,7,8,9,10,11,12,13,14,15]],axis=1,inplace=True)

print(dfp)
print(dft)

dfp.to_sql('players', conn, if_exists='replace')
dft.to_sql('teams', conn, if_exists='replace')

conn.close()
