from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("list", views.list, name="list"),
    path("detail", views.detail, name="detail"),
    path("trash", views.trash, name="trash"),
    path("move_to_trash", views.move_to_trash, name="move_to_trash"),
    path("remove_image", views.remove_image, name="remove_image"),
    path("remove_log", views.remove_log, name="remove_log"),
    path("logout", views.logout_view, name="logout"),
]
