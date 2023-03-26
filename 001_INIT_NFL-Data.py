import sqlite3
import pandas as pd
import nfl_data_py as nfl


def create_nfl_db(years):

    # Definieren der Spalten für Spieler-Info
    columns_R = ['player_id','team', 'player_name', 'position', 'jersey_number', 'status']

    # Daten von API holen
    dfp = nfl.import_rosters(years, columns_R)
    dft = nfl.import_team_desc()
    dfw = nfl.import_weekly_data(years)

    # Nicht verwendete Teamspalten löschen
    dft.drop(dft.columns[[6, 7, 8, 9, 10, 11, 12, 13, 14, 15]], axis=1, inplace=True)
    
    #Neue Spalte id hinzufügen
    dfp.insert(0, 'id', range(1, 1+len(dfp)))
    dft.insert(0, 'id', range(1, 1+len(dft)))
    dfw.insert(0, 'id', range(1, 1+len(dfw)))

    #Spalte id als Inex für Primary_Key nutzen
    dfp.set_index('id', inplace=True)
    dft.set_index('id', inplace=True)
    dfw.set_index('id', inplace=True)

    conn = sqlite3.connect('fantasy.db')

    dfp.to_sql('nfl_player', conn, if_exists='replace', index_label='id')
    dft.to_sql('nfl_team', conn, if_exists='replace',  index_label='id')
    dfw.to_sql('nfl_weekly_stat', conn, if_exists='replace', index_label='id')

    conn.close()



create_nfl_db([2022])