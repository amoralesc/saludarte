from django.urls import path, reverse_lazy


from . import views


app_name = "users"
urlpatterns = [
    # name: users:index, path: /usuarios/
    path("", views.UsersIndexView.as_view(), name="index"),
]
