from django.urls import path

from .views import *

urlpatterns = [
    path('films/', FilmView.as_view(), name='films'),
    path('films/detail/<int:pk>/', FilmDetailView.as_view(), name='film_detail'),
    path('films/create/', FilmCreateView.as_view(), name='create_movie'),
    path('films/delete/<int:pk>/', FilmDeleteView.as_view(), name='delete_movie'),
    path('films/search/', FilmSearchView.as_view(), name='search_movie'),

    # path('films/exemple/', example_form_view, name='film_detail'),

]
