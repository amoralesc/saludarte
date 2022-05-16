from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin

User = get_user_model()


class StaffMemberRequiredMixin(UserPassesTestMixin):
    """Verify that the current user is a staff member."""

    login_url = reverse_lazy("login")

    def test_func(self):
        """
        Only staff members can access this view.
        Redirects to the login page if the user is not authenticated.
        Raises a PermissionDenied exception (403) if the user is not a staff member.
        """
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


class UsersNewView(StaffMemberRequiredMixin, CreateView):
    """
    It shows a form to create a new user.
    """

    model = get_user_model()
    template_name = "users/new_user_form.html"
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

    def get_success_url(self):
        return reverse_lazy("users:index")
