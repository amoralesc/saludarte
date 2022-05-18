from django.urls import path

from . import views


app_name = "medications"
urlpatterns = [
    # name: medications:index, path: /medicamentos/
    path("", views.MedicationsIndexView.as_view(), name="index"),
    # name: medications:create, path: /medicamentos/crear/
    path("crear/", views.create_medication, name="create"),
    # name: medications:delete, path: /medicamentos/<pk>/eliminar/
    path(
        "<int:pk>/eliminar/",
        views.DeleteMedicationView.as_view(),
        name="delete",
    ),
]
