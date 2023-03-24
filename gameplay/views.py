from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import GameSelectionForm

@login_required
def game_selection(request):
    form = GameSelectionForm(user=request.user, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        game_selection = form.save(commit=False)
        game_selection.user = request.user
        game_selection.save()
        form.save_m2m()
        return redirect('game_selection_success')
    return render(request, 'game_selection.html', {'form': form})
