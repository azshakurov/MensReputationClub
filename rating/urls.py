from django.urls import path, include
from django.views.generic import ListView, DetailView
from rating.models import Rating
from . import views


urlpatterns = [
    path(r'', ListView.as_view(
        queryset=Rating.objects.all().order_by("-create_time")[:20],
        template_name="rating/rating.html"
    ), name='rating')
]
