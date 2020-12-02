from django.urls import path

from . import views


urlpatterns = [
    path('search/', views.show_items, name='show_items'),
    path('search/results/', views.show_results, name='show_results'),
]