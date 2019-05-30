from django.shortcuts import render
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import Http404

from .models import Film

class FilmDetailView(DetailView):
    model = Film

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        print(request)
        pk = self.kwargs.get('pk')
        instance = Film.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Film doesn't exist")
        return instance


class FilmListView(ListView):
    template_name = 'film/film_list.html'
    model = Film
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
