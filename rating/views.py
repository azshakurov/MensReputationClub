from django.shortcuts import render
from django.http import HttpResponse

from MRC_site.urls import get_path_name


def rating(request):
    return render(request, 'rating/rating.html', context=get_path_name())

