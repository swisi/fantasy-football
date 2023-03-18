from django.db import models


class NFL_Players(models.Model):

    def __str__(self):
        return f"{self.player_name} ({self.team})"

    id = models.IntegerField(blank=False, null=False, primary_key=True)
    team = models.TextField(blank=True, null=True)
    player_name = models.TextField(blank=True, null=True)
    jersey_number = models.FloatField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nfl_player'

class NFL_Teams(models.Model):

    def __str__(self):
        return f"{self.team_name} ({self.team_abbr})"

    id = models.IntegerField(blank=False, null=False, primary_key=True)
    team_abbr = models.TextField(blank=True, null=True)
    team_name = models.TextField(blank=True, null=True)
    team_id = models.IntegerField(blank=True, null=True)
    team_nick = models.TextField(blank=True, null=True)
    team_conf = models.TextField(blank=True, null=True)
    team_division = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'nfl_team'

class NFL_Stats(models.Model):

    def __str__(self):
        return f"W{self.week} - {self.player_name} - {self.season}"

    id = models.IntegerField(blank=False, null=False, primary_key=True)
    player_id = models.TextField(blank=True, null=True)
    player_name = models.TextField(blank=True, null=True)
    player_display_name = models.TextField(blank=True, null=True)
    position = models.TextField(blank=True, null=True)
    position_group = models.TextField(blank=True, null=True)
    headshot_url = models.TextField(blank=True, null=True)
    recent_team = models.TextField(blank=True, null=True)
    season = models.IntegerField(blank=True, null=True)
    week = models.IntegerField(blank=True, null=True)
    season_type = models.TextField(blank=True, null=True)
    completions = models.IntegerField(blank=True, null=True)
    attempts = models.IntegerField(blank=True, null=True)
    passing_yards = models.FloatField(blank=True, null=True)
    passing_tds = models.IntegerField(blank=True, null=True)
    interceptions = models.FloatField(blank=True, null=True)
    sacks = models.FloatField(blank=True, null=True)
    sack_yards = models.FloatField(blank=True, null=True)
    sack_fumbles = models.IntegerField(blank=True, null=True)
    sack_fumbles_lost = models.IntegerField(blank=True, null=True)
    passing_air_yards = models.FloatField(blank=True, null=True)
    passing_yards_after_catch = models.FloatField(blank=True, null=True)
    passing_first_downs = models.FloatField(blank=True, null=True)
    passing_epa = models.FloatField(blank=True, null=True)
    passing_2pt_conversions = models.IntegerField(blank=True, null=True)
    pacr = models.FloatField(blank=True, null=True)
    dakota = models.FloatField(blank=True, null=True)
    carries = models.IntegerField(blank=True, null=True)
    rushing_yards = models.FloatField(blank=True, null=True)
    rushing_tds = models.IntegerField(blank=True, null=True)
    rushing_fumbles = models.FloatField(blank=True, null=True)
    rushing_fumbles_lost = models.FloatField(blank=True, null=True)
    rushing_first_downs = models.FloatField(blank=True, null=True)
    rushing_epa = models.FloatField(blank=True, null=True)
    rushing_2pt_conversions = models.IntegerField(blank=True, null=True)
    receptions = models.IntegerField(blank=True, null=True)
    targets = models.IntegerField(blank=True, null=True)
    receiving_yards = models.FloatField(blank=True, null=True)
    receiving_tds = models.IntegerField(blank=True, null=True)
    receiving_fumbles = models.FloatField(blank=True, null=True)
    receiving_fumbles_lost = models.FloatField(blank=True, null=True)
    receiving_air_yards = models.FloatField(blank=True, null=True)
    receiving_yards_after_catch = models.FloatField(blank=True, null=True)
    receiving_first_downs = models.FloatField(blank=True, null=True)
    receiving_epa = models.FloatField(blank=True, null=True)
    receiving_2pt_conversions = models.IntegerField(blank=True, null=True)
    racr = models.FloatField(blank=True, null=True)
    target_share = models.FloatField(blank=True, null=True)
    air_yards_share = models.FloatField(blank=True, null=True)
    wopr = models.FloatField(blank=True, null=True)
    special_teams_tds = models.FloatField(blank=True, null=True)
    fantasy_points = models.FloatField(blank=True, null=True)
    fantasy_points_ppr = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'nfl_weekly_stat'

