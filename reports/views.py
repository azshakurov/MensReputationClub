from django.shortcuts import render, reverse
from django.http import HttpResponse

from MRC_site.urls import get_path_name


def reports(request):
    return render(request, 'reports/reports.html', context=get_path_name())


def new(request):
    return render(request, 'reports/new_report.html', context=get_path_name())

