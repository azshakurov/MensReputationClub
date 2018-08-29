"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse
from django.views.generic.base import RedirectView
from django.urls.resolvers import get_resolver


def get_path_name():
    """Collect names of path objects defined in all project urls.py.
    :return: {'name': 'url/of/path/object'}
    """
    p_names = [k for k in get_resolver(None).reverse_dict.keys() if isinstance(k, str)]
    return dict((pn, reverse(pn)) for pn in p_names)


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),

    path('', RedirectView.as_view(url='mrc/'), name='re_mrc'),
    path('mrc/', include('mrc.urls')),

    path('reports/', RedirectView.as_view(url='mrc/'), name='re_reports'),
    path('mrc/reports/', include('reports.urls')),

    path('rating/', RedirectView.as_view(url='mrc/rating/'), name='re_rating'),
    path('mrc/rating/', include('rating.urls'))
]

