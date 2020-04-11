"""Urls posts app"""

from django.urls import path

from posts import views

urlpatterns = [
    path(
        route='posts/',
        view=views.PostsFeedView.as_view(),
        name='feed',
    ),
    path(
        route='posts/new/',
        view=views.create_post,
        name='create',
    ),
    path(
        route='posts/<str:title>',
        view=views.PostDetailView.as_view(),
        name='detail',
    )
]
