from django.urls import path

from . import views


urlpatterns = [
    path('search/zap/', views.show_items_of_zap, name='show_items_of_zap'),
    path('search/ksp/', views.show_items_of_ksp, name='show_items_of_ksp'),
    path('search/results/', views.show_results, name='show_results'),
]