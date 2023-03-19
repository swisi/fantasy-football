from django.shortcuts import render

from .models import NFL_Stats
from .tables import NFLStatsTable

def index(request):
    # Your view logic here
    context = {}
    if request.user.is_authenticated:
        context['is_authenticated'] = True
    
    return render(request, 'index.html',context)

def nfl(request):
    context = {}
    if request.user.is_authenticated:
        context['is_authenticated'] = True

    stats = NFL_Stats.objects.all()
    table = NFLStatsTable(stats)
    return render(request, 'stats.html', {'table': table, 'context': context})