import django_tables2 as tables
from django_filters.views import FilterView
from .models import NFL_Stats

# ---> TABELLEN
class NFLStatsTable(tables.Table, FilterView):
    class Meta:
        template_name = "django_tables2/bootstrap5.html"
        model = NFL_Stats
        fields = (
            'season', 
            'week', 
            'player_name', 
            'position', 
            'fantasy_points', 
            'fantasy_points_ppr',
            )
        