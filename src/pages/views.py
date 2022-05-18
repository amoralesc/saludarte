from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    """
    Default home page located at /
    """

    return render(request, "pages/home.html")
