from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse

from .models import NFL_Stats

def index(request):
    # Your view logic here
    context = {}
    if request.user.is_authenticated:
        context['is_authenticated'] = True
    
    return render(request, 'index.html',context)

def fetchstats(request):
    object_list = NFL_Stats.objects.all()
    json = serializers.serialize('json', object_list)
    return HttpResponse(json, content_type='application/json')


def nfl(request):
    context = {}
    if request.user.is_authenticated:
        context['is_authenticated'] = True

    stats = NFL_Stats.objects.all()
    
    return render(request, 'stats.html', {'stats': stats, 'context': context})