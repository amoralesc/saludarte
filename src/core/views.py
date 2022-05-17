from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy


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
