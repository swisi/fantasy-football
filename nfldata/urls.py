from django.urls import path
from . import views


urlpatterns = [
    path('', views.nfl, name='stats'), # Leere /nfl/ Url wird auf /nfl/stats weitergeleitet
    path('stats/', views.nfl, name='stats'),
    ]
