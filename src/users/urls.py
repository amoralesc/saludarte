from django.urls import path


from . import views


app_name = "users"
urlpatterns = [
    # name: users:index, path: /usuarios/
    path("", views.UsersIndexView.as_view(), name="index"),
]
