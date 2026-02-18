from django.contrib.auth import views as auth_views
from .forms import PagesLoginForm
from django.urls import path, include

urlpatterns = [
  # path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
  path("login/", auth_views.LoginView.as_view(template_name="registration/login.html", authentication_form=PagesLoginForm), name="login"),
]
