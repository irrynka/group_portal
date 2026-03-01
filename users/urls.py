from django.urls import path
from users import views

urlpatterns = [
    path("", views.Index, name="index"),

    path("poll/", views.Poll_List.as_view(), name="poll_list"),
    path("poll/<int:pk>/", views.Poll_Detail.as_view(), name="poll_detail"),
    path("poll/create/", views.Poll_Create.as_view(), name="poll_create"),
    path("poll/<int:pk>/vote/", views.Poll_Vote.as_view(), name="poll_vote"),

    

    path("portfolio/", views.Portfolio_List.as_view(), name="portfolio_list"),
    path("portfolio/create/", views.Portfolio_Create.as_view, name="portfolia_create"),
    path("portfolio/<int:pk>/delete/", views.Portfolio_Delete.as_view, name="portfolia_delete"),

    path("portfolio/<int:portfolio_id>/add-file/", views.Portfolio_File_Add.as_view(), name="portfolio_add_file"),
    path("portfolio/<int:portfolio_id>/add-url/", views.Portfolio_Url_Add.as_view(), name="porfolio_add_url"),

    path("media/<int:pk>/delete/", views.Portfolio_Media_Delete.as_view(), name="media_delete"),

    path("grades/", views.Grade_List.as_view(), name="grade_list"),
    path("grades/create/", views.Grade_Create.as_view(), name="grade_create"),
    path("grades/<int:pk>/edit/", views.Grade_Update.as_view(), name="grade_update"),
    path("grades/<int:pk>/delete/", views.Grade_Delete.as_view(), name="grade_delete"),

    path("galery/", views.Galery_List.as_view(), name='galery_list'),
    path("galery/upload/", views.Galery_Upload.as_view(), name='galery_upload'),
    path("galery/moderate/", views.Gallery_Moderation.as_view(), name='galery_moderate'),
    path("galery/<int:pk>/approve/", views.Galery_Approve.as_view(), name='galery_approve'),
    path("galery/<int:pk>/reject/", views.Galery_Delete.as_view(), name='galery_delete'),
    

    
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),

]

