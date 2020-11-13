from django.urls import path

from . import views


urlpatterns = [
    path('search/', views.SearchResultsView, name='search_results'),
]