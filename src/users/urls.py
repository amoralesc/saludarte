from django.urls import path


from . import views


app_name = "users"
urlpatterns = [
    # name: users:index, path: /usuarios/
    path("", views.UsersIndexView.as_view(), name="index"),
    # name: users:view, path: /usuarios/<pk>/,
    path("<int:pk>/", views.UserDetailView.as_view(), name="view"),
    # name: users:new, path: /usuarios/nuevo/
    path("nuevo/", views.NewUserView.as_view(), name="new"),
    # name: users:edit, path: /usuarios/<pk>/editar/
    path("<int:pk>/editar/", views.EditUserView.as_view(), name="edit"),
    # name: users:delete, path: /usuarios/<user_id>/eliminar/
    path("<int:user_id>/eliminar/", views.delete_user, name="delete"),
]
