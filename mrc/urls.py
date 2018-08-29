from django.urls import path, include

from . import views


urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'ruls/', views.ruls, name='ruls'),
]

