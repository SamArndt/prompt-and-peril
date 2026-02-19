from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm


class SignUpView(CreateView):
    form_class = UserCreationForm 
    """
    for all generic class-based views, the URLs are not loaded when the file is imported,
    so we have to use the lazy form of reverse to load them later when we are sure they're available.
    """
    success_url = reverse_lazy("accounts:login")
    template_name = "registration/signup.html"

