from django.contrib.auth import get_user_model
from django.views.generic import ListView

User = get_user_model()


class UsersIndexView(ListView):
    template_name = "users/index.html"
    context_object_name = "users"

    def get_queryset(self):
        """
        Returns all the users in the database.
        (not including the currently authenticated user).
        """
        return User.objects.exclude(pk=self.request.user.pk)
