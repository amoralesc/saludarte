from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm

from django.http import (
    HttpResponseNotAllowed,
    HttpResponseRedirect,
)
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from core.views import StaffMemberRequiredMixin


User = get_user_model()


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


class DetailUserView(StaffMemberRequiredMixin, DetailView):
    """
    It shows the details of a specific user.
    Offers actions to edit the user:
    - Edit the user's information
    - Delete the user
    """

    model = get_user_model()
    template_name = "users/detail_user.html"


class NewUserView(StaffMemberRequiredMixin, CreateView):
    """
    It allows a staff user to create a new user.
    It shows a form to input the user's data.
    It also sends a welcome email to the user with
    a link to reset their password.
    """

    model = get_user_model()
    template_name = "users/new_user.html"
    # The password is not included because it is left blank when a new
    # user is created. The welcome email has a link to reset the password.
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
        messages.success(
            self.request, "El usuario ha sido creado exitosamente."
        )
        return reverse_lazy("users:index")

    def form_valid(self, form):
        """
        If user creation form was valid, sends a welcome email
        to the user with a link to reset their password.
        Also calls super to save the user in the database.
        """

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
    template_name = "users/edit_user.html"
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


class DeleteUserView(StaffMemberRequiredMixin, DeleteView):
    """
    Deletes an user given its id.
    """

    model = get_user_model()

    def get_success_url(self):
        messages.success(
            self.request, "El usuario ha sido eliminado exitosamente."
        )
        return reverse_lazy("users:index")
