from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView

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

    template_name = "residents/index.html"
    model = Resident
    context_object_name = "residents"
