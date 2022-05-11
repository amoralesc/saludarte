import os

from django import get_version
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    context = {
        "debug": settings.DEBUG,
        "django_ver": get_version(),
        "python_ver": os.environ["PYTHON_VERSION"],
    }

    return render(request, "pages/home.html", context)
