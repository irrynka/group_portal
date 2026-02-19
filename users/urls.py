from django.urls import path
from users import views

urlpatterns = [
    path("", views.index, name="index"),
    path("poll/", views.poll_list.as_view(), name="poll_list"),
    path("poll_add/", views.poll_create.as_view(), name="poll_add"),

]

