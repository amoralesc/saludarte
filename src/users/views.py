from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.mixins import (
    #    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

User = get_user_model()


class StaffMemberRequiredMixin(UserPassesTestMixin):
    """Verify that the current user is a staff member."""

    raise_exception = False
    login_url = reverse_lazy("login")

    # Only authenticated staff users can access this view
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff


class UsersIndexView(StaffMemberRequiredMixin, ListView):
    """
    It shows a list of all the users in the database.
    Offers actions to edit the users:
    - Create a new user
    - View an existing user
    - Edit an existing user
    - Delete an existing user
    """

    template_name = "users/index.html"
    context_object_name = "users"

    def get_queryset(self):
        """
        Returns all the users in the database.
        (not including the currently authenticated user).
        """
        return User.objects.exclude(pk=self.request.user.pk)
