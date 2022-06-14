from django.urls import re_path
from movie import views

urlpatterns = [
    re_path(r"^api/v1/add-movie/", views.CreateMovieInfoAPiView.as_view()),
    re_path(r"^api/v1/movies/", views.MovieListAPiView.as_view()),
]