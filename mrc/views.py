from django.shortcuts import render
from django.http import HttpResponse

from MRC_site.urls import get_path_name


def index(request):
    return render(request, 'mrc/mrc.html', context=get_path_name())


def ruls(request):
    return render(request, 'mrc/ruls.html', context=get_path_name())

