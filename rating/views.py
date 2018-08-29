from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from rating.models import Rating

from MRC_site.urls import get_path_name


class RatingListView(ListView):

    model = Rating
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_path_name())
        return context

