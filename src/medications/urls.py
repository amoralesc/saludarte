from django.urls import path

from . import views


app_name = "medications"
urlpatterns = [
    # name: medications:index, path: /medicamentos/
    path("", views.MedicationsIndexView.as_view(), name="index"),
]
