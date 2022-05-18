from django.urls import path

from . import views


app_name = "users"
urlpatterns = [
    # name: users:index, path: /usuarios/
    path("", views.UsersIndexView.as_view(), name="index"),
    # name: users:detail, path: /usuarios/<pk>/,
    path("<int:pk>/", views.DetailUserView.as_view(), name="detail"),
    # name: users:new, path: /usuarios/nuevo/
    path("nuevo/", views.NewUserView.as_view(), name="new"),
    # name: users:edit, path: /usuarios/<pk>/editar/
    path("<int:pk>/editar/", views.EditUserView.as_view(), name="edit"),
    # name: users:update_is_active, path: /usuarios/<pk>/cambiar_estado/
    path(
        "<int:pk>/cambiar_estado/",
        views.UpdateUserIsActiveView.as_view(),
        name="update_is_active",
    ),
    # name: users:delete, path: /usuarios/<pk>/eliminar/
    path("<int:pk>/eliminar/", views.DeleteUserView.as_view(), name="delete"),
]
