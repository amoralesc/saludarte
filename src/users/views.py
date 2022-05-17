from django.contrib.auth import get_user_model

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.http import (
    HttpResponseNotAllowed,
    HttpResponseRedirect,
)
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.forms import PasswordResetForm

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
        (not including the currently authenticated user nor superusers).
        """
        return User.objects.exclude(pk=self.request.user.pk).exclude(
            is_superuser=True
        )


class UserDetailView(StaffMemberRequiredMixin, DetailView):
    """
    It shows the details of a specific user.
    Offers actions to edit the user:
    - Edit the user
    - Delete the user
    """

    model = get_user_model()
    template_name = "users/view_user.html"


class NewUserView(StaffMemberRequiredMixin, CreateView):
    """
    It allows a staff user to create a new user.
    It shows a form to input the user's data.
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

    def form_valid(self, form):
        """
        If user creation form was valid, sends a welcome email
        to the user with a link to reset their password.
        Also calls super to save the user in the database.
        """

        messages.success(
            self.request, "El usuario ha sido creado exitosamente."
        )
        redirect = super().form_valid(form)

        # Create a password reset form with the email of the new user.
        password_reset_form = PasswordResetForm(
            {"email": form["email"].value()}
        )

        # Send the welcome email with the password reset link.
        password_reset_form.is_valid()
        password_reset_form.save(
            request=self.request,
            use_https=self.request.is_secure(),
            subject_template_name="users/new_user_email_subject.txt",
            email_template_name="users/new_user_email.html",
        )

        return redirect


class EditUserView(StaffMemberRequiredMixin, UpdateView):
    """
    It allows a staff user to update an existing user.
    It shows a form to edit the user's data.
    """

    model = get_user_model()
    template_name = "users/edit_user_form.html"
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


class UpdateUserIsActiveView(StaffMemberRequiredMixin, UpdateView):
    """
    If called, it updates the is_active field of the user to its
    opposite.
    """

    http_method_names = ["post"]
    model = get_user_model()
    fields = ["is_active"]

    # Redirect to the path in next or defaults to the users index.
    def get_success_url(self):
        return self.request.POST.get("next", reverse_lazy("users:index"))


@staff_member_required(login_url=reverse_lazy("login"))
def delete_user(request, user_id):
    """
    Deletes an user given its id.
    """

    if request.method == "POST" or request.method == "DELETE":
        user = get_object_or_404(User, pk=user_id)
        user.delete()
        messages.success(request, "El usuario ha sido eliminado exitosamente.")
        return HttpResponseRedirect(reverse_lazy("users:index"))
    else:
        return HttpResponseNotAllowed(["post", "delete"])
