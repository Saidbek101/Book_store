from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

from .forms import CustomAuthenticationForm


class AccountLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "account/login.html"
    next_page = 'account:profile'
    

class CustomLogutView(LogoutView):
    next_page = 'books:homepage'


class ProfileView(TemplateView):
    template_name = 'account/profile.html'