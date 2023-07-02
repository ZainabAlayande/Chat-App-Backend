from django.urls import path
from . import views

#  http://127.0.0.1:8000/converse/register/
urlpatterns = [
    path("register/", views.AuthenticationView.as_view(), name="post"),
    path("update_profile/<str:username>", views.ProfileView.as_view(), name="update_profile"),
    path("search_by_username/<str:username>", views.ProfileView.as_view(), name="update_profile"),
    path("edit_profile/<str:username>", views.ProfileView.as_view(), name="edit_profile"),
    path("edit_username/<str:username>", views.ProfileView.as_view(), name="edit_username"),
    path("edit_password/<str:username>", views.ProfileView.as_view(), name="edit_password"),
]
