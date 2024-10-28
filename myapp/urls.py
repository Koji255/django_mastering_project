from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("authorization/", views.authorization, name="authorization"),
    path("get_users/", views.get_users, name="get_users"),
]