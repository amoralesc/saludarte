from django.urls import path

from . import views


app_name = "residents"
urlpatterns = [
    # name: residents:index, path: /residentes/
    path("", views.ResidentsIndexView.as_view(), name="index"),
    # name: residents:new, path: /residentes/nuevo/
    path("nuevo/", views.NewResidentView.as_view(), name="new"),
    # name: residents:delete, path: /residentes/<resident_id>/eliminar/
    path("<int:resident_id>/eliminar/", views.delete_resident, name="delete"),
]
