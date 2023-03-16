# myapp/admin.py

from django.contrib import admin
from .models import NFLTeams, NFLPlayers, NFLStats
import sqlite3
import pandas as pd
import nfl_data_py as nfl


def create_nfl_team_db():

    dft = nfl.import_team_desc()
    dft.drop(dft.columns[[6, 7, 8, 9, 10, 11, 12, 13, 14, 15]], axis=1, inplace=True)
    dft.rename(columns = {'team_id':'id'}, inplace = True)

    conn = sqlite3.connect('fantasy.db')

    dft.to_sql('nfl_teams', conn, if_exists='replace')

    conn.close()
create_nfl_team_db.short_description = "Create NFL database"

def create_nfl_player_db():
    years = [2022]  # Change this to use other years if needed
    columns_R = ['plaxer_id','team', 'player_name', 'jersey_number', 'status']
     
    dfp = nfl.import_rosters(years, columns_R)
    dfp.rename(columns = {'player_id':'id'}, inplace = True)

    conn = sqlite3.connect('fantasy.db')

    dfp.to_sql('nfl_players', conn, if_exists='replace')

    conn.close()
create_nfl_player_db.short_description = "Create NFL database"

def create_nfl_stats_db():
    years = [2022]  # Change this to use other years if needed

    dfw = nfl.import_weekly_data(years)

    conn = sqlite3.connect('fantasy.db')

    dfw.to_sql('nfl_stats', conn, if_exists='replace')

    conn.close()
create_nfl_stats_db.short_description = "Create NFL database"

class NFLTeamsAdmin(admin.ModelAdmin):
    actions = [create_nfl_team_db]

class NFLPlayersAdmin(admin.ModelAdmin):
    actions = [create_nfl_player_db]

class NFLStatsAdmin(admin.ModelAdmin):
    actions = [create_nfl_stats_db]

admin.site.register(NFLTeams, NFLTeamsAdmin)
admin.site.register(NFLPlayers, NFLPlayersAdmin)
admin.site.register(NFLStats,NFLStatsAdmin)

