from django.urls import path

from . import views


app_name = "medications"
urlpatterns = [
    # name: medications:index, path: /medicamentos/
    path("", views.MedicationsIndexView.as_view(), name="index"),
    # name: medications:new, path: /medicamentos/nuevo/
    path("nuevo/", views.create_medication, name="new"),
    # name: medications:edit, path: /medicamentos/<pk>/editar/
    path("<int:pk>/editar/", views.edit_medication, name="edit"),
    # name: medications:delete, path: /medicamentos/<pk>/eliminar/
    path(
        "<int:pk>/eliminar/",
        views.DeleteMedicationView.as_view(),
        name="delete",
    ),
]
