from django.urls import path
from users import views

urlpatterns = [
    path("", views.index, name="index"),
    path("poll/", views.poll_list.as_view(), name="poll_list"),
    # path("poll_add/", views.poll_create.as_view(), name="poll_add"),

    path("portfolio/", views.portfolio_list.as_view(), name="portfolio_list"),
    path("portfolio/create/", views.portfolio_create.as_view, name="portfolia-create"),
    path("portfolio/delete/", views.portfolio_delete.as_view, name="portfolia-delete"),

    path("portfolio/add-file", views.portfolio_file_add.as_view(), name="portfolio_add_file"),
    path("portfolio/add-url", views.portfolio_url_add.as_view(), name="porfolio_add_url"),

    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),

]

