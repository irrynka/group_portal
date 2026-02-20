from django.urls import path
from users import views

urlpatterns = [
    path("", views.index, name="index"),
    path("poll/", views.poll_list.as_view(), name="poll_list"),
    path("poll_add/", views.poll_create.as_view(), name="poll_add"),

    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),

]

