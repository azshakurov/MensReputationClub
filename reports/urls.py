from django.urls import path, include

from . import views


urlpatterns = [
    path(r'', views.reports, name='reports'),
    path(r'new_report/', views.new, name='new_report'),
]

