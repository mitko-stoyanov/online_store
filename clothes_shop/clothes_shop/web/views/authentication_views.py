from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from clothes_shop.web.forms import UserRegistrationForm, UserLoginForm, ChangePasswordForm
from clothes_shop.web.models import AppUser


class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'profile/register.html'
    success_url = reverse_lazy('index')

    # after the registration the user is logged in!
    def form_valid(self, *args, **kwargs):
        result = super().form_valid(*args, **kwargs)
        login(self.request, self.object)
        return result


class UserLoginView(LoginView):
    template_name = 'profile/login.html'
    form_class = UserLoginForm

    def get_success_url(self):
        return reverse_lazy('index')


class UerLogoutView(LogoutView):
    next_page = reverse_lazy('index')


class ChangePasswordView(PasswordChangeView):
    template_name = 'profile/change-password.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('profile')


class DeleteProfileView(DeleteView):
    model = AppUser
    template_name = 'profile/delete-profile.html'
    success_url = reverse_lazy('register')