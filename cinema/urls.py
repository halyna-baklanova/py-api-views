from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet
)

router = routers.DefaultRouter()

router.register("movie", MovieViewSet)

cinemahall_list = CinemaHallViewSet.as_view(
    actions={
        "get": "list",
        "post": "create",
    }
)

cinemahall_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

movie_list = MovieViewSet.as_view(
    actions={
        "get": "list",
        "post": "create",
    }
)

movie_detail = MovieViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

urlpatterns = [
    path(
        "genres/",
        GenreList.as_view(),
        name="genre_list"
    ),
    path(
        "genres/<int:pk>/",
        GenreDetail.as_view(),
        name="genre_detail"
    ),
    path(
        "actors/",
        ActorList.as_view(),
        name="actor_list"
    ),
    path(
        "actor/<int:pk>/",
        ActorDetail.as_view(),
        name="actor_detail"
    ),
    path(
        "cinemahalls/",
        cinemahall_list,
        name="cinemahall_list"
    ),
    path(
        "cinemahall/<int:pk>/",
        cinemahall_detail,
        name="cinemahall_detail"
    ),
    path(
        "movies/",
        include(router.urls),
        name="movie_list"
    ),
    path(
        "movies/<int:pk>/",
        include(router.urls),
        name="movie_detail"
    ),
]

app_name = "cinema"
