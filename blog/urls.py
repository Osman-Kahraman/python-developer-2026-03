"""
URL configuration for blog pages.
"""

from django.urls import path

from . import views

urlpatterns = [
    path("posts/", views.index, name="index"),
    path("posts/<uuid:post_id>/", views.post_detail, name="post_detail"),
    path("", views.welcome, name="welcome"),
]
