from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from django.urls import reverse_lazy

from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Resident, Relative
from .views import OnlyAccessMySiteResidentsMixin


class NewRelativeView(LoginRequiredMixin, CreateView):
    """
    It shows a form to create a new relative.
    """

    model = Relative
    template_name = "residents/new_relative.html"
    fields = [
        "first_name",
        "last_name",
        "identification_type",
        "identification_number",
        "gender",
        "kinship",
        "email",
        "contact_number",
        "email_alerts",
        "whatsapp_alerts",
    ]

    def form_valid(self, form):
        resident = get_object_or_404(Resident, pk=self.kwargs["pk"])
        form.instance.resident = resident
        return super(NewRelativeView, self).form_valid(form)

    def get_success_url(self):
        messages.success(
            self.request, "El familiar ha sido creado exitosamente."
        )
        return (
            reverse_lazy("residents:detail", kwargs={"pk": self.kwargs["pk"]})
            + "?page=2"
        )


class EditRelativeView(
    LoginRequiredMixin, OnlyAccessMySiteResidentsMixin, UpdateView
):
    """
    It shows a form to edit an existing relative.
    """

    model = Relative
    template_name = "residents/edit_relative.html"
    fields = [
        "first_name",
        "last_name",
        "identification_type",
        "identification_number",
        "gender",
        "kinship",
        "email",
        "contact_number",
        "email_alerts",
        "whatsapp_alerts",
    ]

    def get_object(self):
        return Relative.objects.get(pk=self.kwargs["relative_pk"])

    def get_success_url(self):
        url = super(UpdateView, self).get_success_url()
        messages.success(
            self.request, "El familiar ha sido editado exitosamente."
        )
        return url


class DeleteRelativeView(
    LoginRequiredMixin, OnlyAccessMySiteResidentsMixin, DeleteView
):
    """
    Deletes a relative given its id.
    """

    model = Resident

    def get_object(self):
        return Relative.objects.get(pk=self.kwargs["relative_pk"])

    def get_success_url(self):
        messages.success(
            self.request, "El familiar ha sido eliminado exitosamente."
        )
        return (
            reverse_lazy("residents:detail", kwargs={"pk": self.kwargs["pk"]})
            + "?page=2"
        )
