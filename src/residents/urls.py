from django.urls import path

from . import views

app_name = "residents"
urlpatterns = [
    # name: residents:index, path: /residentes/
    path("", views.ResidentsIndexView.as_view(), name="index"),
    # name: residentes:new, path: /residentes/nuevo/
    path("nuevo/", views.NewResidentView.as_view(), name="new"),
]
