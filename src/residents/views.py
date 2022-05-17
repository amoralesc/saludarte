from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView

from .models import Resident


class ResidentsIndexView(LoginRequiredMixin, ListView):
    """
    It shows a list of all the residents in the database.
    Offers actions to alter the users:
    - Create a new resident
    - View an existing resident
    - Edit an existing resident
    - Delete an existing resident
    """

    model = Resident
    context_object_name = "residents"
    template_name = "residents/index.html"


class NewResidentView(LoginRequiredMixin, CreateView):
    """
    It shows a form to create a new resident.
    """

    model = Resident
    template_name = "residents/new_resident_form.html"

    def get_success_url(self):
        return reverse_lazy("residents:index")

    fields = [
        "first_name",
        "last_name",
        "email",
        "identification_type",
        "identification_number",
        "gender",
        "is_staff",
        "site",
    ]
