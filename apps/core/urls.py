from django.urls import path

from .views import SearchViewElk

urlpatterns = [
    path("search/", SearchViewElk.as_view()),
]
