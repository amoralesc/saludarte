from django.urls import path

from . import views


app_name = "accounts"
urlpatterns = [
    # /accounts/profile
    path("profile/", views.ProfilePageView.as_view(), name="profile"),
]
