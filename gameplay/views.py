from django_datatables_view.base_datatable_view import BaseDatatableView
from django.shortcuts import render
from django.utils.html import escape
from nfldata.models import  NFL_Players
from .models import GamePlay

class GamePlayView(BaseDatatableView):
    model = GamePlay
    columns = ['week_number', 'qb', 'rb', 'wr', 'te', 'k', 'qb_backup', 'rb_backup', 'wr_backup', 'te_backup', 'k_backup']

    def get_initial_queryset(self):
        return self.model.objects.filter(user=self.request.user).order_by('week_number')

    def render_column(self, row, column):
        # Customize rendering of columns
        if column in ['qb', 'rb', 'wr', 'te', 'k', 'qb_backup', 'rb_backup', 'wr_backup', 'te_backup', 'k_backup']:
            player_field = getattr(row, column)
            player_name = str(player_field) if player_field else ''
            options = ''.join([f'<option value="{player.id}">{escape(str(player))}</option>'
                               for player in NFL_Players.objects.filter(position__iexact=column)])
            return f'<select class="form-control" name="{column}"><option value=""></option>{options}</select>'

        # Default rendering
        return super(GamePlayView, self).render_column(row, column)


def game_selection(request):
    # Implement your view logic here
    return render(request, 'game_selection.html')