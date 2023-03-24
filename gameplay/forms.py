from django import forms
from nfldata.models import NFL_Players

class GameSelectionForm(forms.Form):
    week = forms.IntegerField(min_value=1, max_value=20)
    qb = forms.ModelChoiceField(queryset=NFL_Players.objects.filter(position='QB'))
    rb = forms.ModelChoiceField(queryset=NFL_Players.objects.filter(position='RB'))
    wr = forms.ModelChoiceField(queryset=NFL_Players.objects.filter(position='WR'))
    te = forms.ModelChoiceField(queryset=NFL_Players.objects.filter(position='TE'))
    k = forms.ModelChoiceField(queryset=NFL_Players.objects.filter(position='K'))
