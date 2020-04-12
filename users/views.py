"""Users views"""

# Django
from django.contrib.auth import (
    login,
    logout,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.generic import DetailView, FormView, UpdateView

# Models
from django.contrib.auth.models import User
from users.models import Profile
from posts.models import Post

# Forms
from users.forms import SignupForm


class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view."""

    template_name = 'users/detail.html'
    queryset = User.objects.all()
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-createdAt')  # NOQA
        return context


class LoginView(auth_views.LoginView):
    """Login view"""
    template_name = 'users/login.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout user."""
    template_name = 'users/logout.html'


class SignupFormView(FormView):
    """Signup user account"""
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile user."""

    template_name = 'users/profile.html'
    model = Profile
    fields = ['biography', 'website', 'phone_number', 'picture']

    def get_object(self):
        """Return user's profile"""
        return self.request.user.profile

    def get_success_url(self):
        """Return to profile user."""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})
