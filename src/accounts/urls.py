from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views


from . import views


app_name = "accounts"
urlpatterns = [
    # name: accounts:profile, path: /cuenta/perfil/
    path("perfil/", views.ProfilePageView.as_view(), name="profile"),
    # name: accounts:edit_profile, path /cuenta/editar_perfil/
    path(
        "editar_perfil/",
        views.EditProfilePageView.as_view(),
        name="edit_profile",
    ),
    # name: accounts:password_change, path: /cuenta/cambiar_contraseña/
    path(
        "cambiar_contraseña/",
        auth_views.PasswordChangeView.as_view(
            template_name="accounts/password_change_form.html",
            success_url=reverse_lazy("accounts:password_change_done"),
        ),
        name="password_change",
    ),
    # name: accounts:password_change_done, path: /cuenta/cambiar_contraseña/hecho/
    path(
        "cambiar_contraseña/hecho/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="accounts/password_change_done.html",
        ),
        name="password_change_done",
    ),
]
