from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.contrib.auth import get_user_model


class ProfilePageView(LoginRequiredMixin, DetailView):
    """
    It shows the profile page of the user. It includes all the information
    about the user, and some links to edit the user's profile.
    """

    model = get_user_model()
    template_name = "accounts/profile.html"

    # The context_object is the current authenticated user
    def get_object(self, queryset=None):
        return self.request.user
