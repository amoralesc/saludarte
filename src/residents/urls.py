from django.urls import path

from . import views


app_name = "residents"
urlpatterns = [
    # name: residents:index, path: /residentes/
    path("", views.ResidentsIndexView.as_view(), name="index"),
    # name: users:detail, path: /residentes/<pk>/,
    path("<int:pk>/", views.DetailResidentView.as_view(), name="detail"),
    # name: residents:new, path: /residentes/nuevo/
    path("nuevo/", views.NewResidentView.as_view(), name="new"),
    # name: residents:edit, path: /residentes/<pk>/editar/
    path("<int:pk>/editar/", views.EditResidentView.as_view(), name="edit"),
    # name: residents:delete, path: /residentes/<pk>/eliminar/
    path(
        "<int:pk>/eliminar/",
        views.DeleteResidentView.as_view(),
        name="delete",
    ),
]
