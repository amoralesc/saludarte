from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView
from django.contrib.auth import get_user_model


class ProfilePageView(LoginRequiredMixin, DetailView):
    """
    It shows the profile page of the user. It includes all the information
    about the user, and some links to edit the user's profile.
    """

    model = get_user_model()
    template_name = "accounts/profile.html"

    # The context_object is the currently authenticated user
    def get_object(self, queryset=None):
        return self.request.user


class EditProfilePageView(LoginRequiredMixin, UpdateView):
    """
    It allows the user to edit his profile.
    """

    model = get_user_model()
    template_name = "accounts/edit_profile_form.html"
    fields = [
        "first_name",
        "last_name",
        "email",
        "identification_type",
        "identification_number",
        "gender",
    ]

    def get_success_url(self):
        return reverse("accounts:profile")

    # The context_object is the currently authenticated user
    def get_object(self, queryset=None):
        return self.request.user
