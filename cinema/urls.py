from django.urls import path

from cinema.views import (
    GenreList,
    GenreDetail,
    movie_list,
    movie_detail,
    ActorList,
    ActorDetail,
)

urlpatterns = [
    path(
        "api/cinema/genres/",
        GenreList.as_view(),
        name="genre-list"
    ),
    path(
        "api/cinema/genres/<int:pk>/",
        GenreDetail.as_view(),
        name="genre-detail"
    ),
path(
        "api/cinema/actors/",
        ActorList.as_view(),
        name="actor-list"
    ),
    path(
        "api/cinema/actor/<int:pk>/",
        ActorDetail.as_view(),
        name="actor-detail"
    ),
    path(
        "movies/",
        movie_list,
        name="movie-list"
    ),
    path(
        "movies/<int:pk>/",
        movie_detail,
        name="movie-detail"
    ),
]

app_name = "cinema"
