from django.shortcuts import render

from .models import NFL_Stats
from .tables import NFLStatsTable

def index(request):
    # Your view logic here
    return render(request, 'index.html')

def nfl(request):
    stats = NFL_Stats.objects.all()
    table = NFLStatsTable(stats)
    return render(request, 'stats.html', {'table': table})