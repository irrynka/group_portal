from django.urls import path
from users import views

urlpatterns = [
    path("/", views.poll_list.as_view(), name="poll"),
    path("/poll_add", views.poll_create.as_view(), name="poll_add"),
]

