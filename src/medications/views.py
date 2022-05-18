from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    #    CreateView,
    #    UpdateView,
    #    DeleteView,
)

from .models import Medication


class MedicationsIndexView(LoginRequiredMixin, ListView):
    """
    It shows a list of all the medications in the database.
    Offers actions to alter the medications:
    - Create a new medication
    - Edit an existing medication
    - Delete an existing medication
    """

    model = Medication
    context_object_name = "medications"
    template_name = "medications/index.html"