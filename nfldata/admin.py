# myapp/admin.py

from django.contrib import admin
from .models import NFL_Teams, NFL_Players, NFL_Stats
import sqlite3
import pandas as pd
import nfl_data_py as nfl

season = 2022

def create_nfl_team_db(modeladmin, request, queryset):

    dft = nfl.import_team_desc()
    dft.drop(dft.columns[[6, 7, 8, 9, 10, 11, 12, 13, 14, 15]], axis=1, inplace=True)
    dft.insert(0, 'id', range(1, 1+len(dft)))
    dft.set_index('id', inplace=True)

    conn = sqlite3.connect('fantasy.db')

    dft.to_sql('nfl_team', conn, if_exists='replace',  index_label='id')

    conn.close()
create_nfl_team_db.short_description = "Update NFL Team Info"

def create_nfl_player_db(modeladmin, request, queryset):
    years = [season]  # Change this to use other years if needed
    columns_R = ['player_id','team', 'player_name', 'position', 'jersey_number', 'status']
     
    dfp = nfl.import_rosters(years, columns_R)
    dfp.insert(0, 'id', range(1, 1+len(dfp)))
    dfp.set_index('id', inplace=True)
      
    conn = sqlite3.connect('fantasy.db')

    dfp.to_sql('nfl_player', conn, if_exists='replace', index_label='id')

    conn.close()
create_nfl_player_db.short_description = "Update NFL Player Info"

def create_nfl_stats_db(modeladmin, request, queryset):
    years = [season]  # Change this to use other years if needed

    dfw = nfl.import_weekly_data(years)
    dfw.insert(0, 'id', range(1, 1+len(dfw)))
    dfw.set_index('id', inplace=True)

    conn = sqlite3.connect('fantasy.db')

    dfw.to_sql('nfl_weekly_stat', conn, if_exists='replace', index_label='id')

    conn.close()
create_nfl_stats_db.short_description = "Update NFL Weekly Stats"


def delete_team(modeladmin, request, queryset):
    conn = sqlite3.connect('fantasy.db')
    c = conn.cursor()
    c.execute("DELETE FROM nfl_team WHERE team_abbr NOT IN ('TEN')")
    conn.commit()
    conn.close()
delete_team.short_description = "Delete all Teams except TEN"


def delete_player(modeladmin, request, queryset):
    conn = sqlite3.connect('fantasy.db')
    c = conn.cursor()
    c.execute("DELETE FROM nfl_player WHERE team NOT IN ('TEN')")
    conn.commit()
    conn.close()
delete_player.short_description = "Delete selected players or all Players except TEN if no selection"

def delete_weekly_stats(modeladmin, request, queryset):
    conn = sqlite3.connect('fantasy.db')
    c = conn.cursor()
    c.execute("DELETE FROM nfl_weekly_stat WHERE player_id NOT IN (SELECT player_id FROM nfl_player)")
    conn.commit()
    conn.close()
delete_weekly_stats.short_description = "Delete all stats for existing players"


class NFLTeamsAdmin(admin.ModelAdmin):
    actions = [create_nfl_team_db, delete_team]

class NFLPlayersAdmin(admin.ModelAdmin):
    actions = [create_nfl_player_db, delete_player]

class NFLStatsAdmin(admin.ModelAdmin):
    actions = [create_nfl_stats_db, delete_weekly_stats]

admin.site.register(NFL_Teams, NFLTeamsAdmin)
admin.site.register(NFL_Players, NFLPlayersAdmin)
admin.site.register(NFL_Stats,NFLStatsAdmin)

