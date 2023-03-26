from django.urls import path
from .views import GamePlayView


urlpatterns = [
    path('', GamePlayView.as_view(), name='gameplay'),
    ]
