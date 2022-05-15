from django.urls import path

from . import views


app_name = "accounts"
urlpatterns = [
    # name: accounts:profile, path: /cuenta/perfil
    path("perfil/", views.ProfilePageView.as_view(), name="profile"),
]
