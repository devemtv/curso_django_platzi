"""Posts views."""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy

# Forms
from posts.forms import PostForm

# Models
from posts.models import Post


class PostDetailView(LoginRequiredMixin, DetailView):
    """Detail post user."""

    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    slug_field = 'pk'
    slug_url_kwarg = 'pk'


class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-createdAt',)
    paginate_by = 15
    context_object_name = 'posts'


class CreatePostView(LoginRequiredMixin, CreateView):
    """Create post new views"""

    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context"""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context
