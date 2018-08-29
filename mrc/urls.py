from django.urls import path, include

from mrc.views import index, ruls


urlpatterns = [
    path(r'', index, name='index'),
    path(r'ruls/', ruls, name='ruls'),
]

