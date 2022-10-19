from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomChangeUserForm
from django.contrib.auth.models import User
from .models import BlogTag, BlogPost

class HomeView(ListView):
    template_name = 'index.html'

    def get_queryset(self, *args, **kwargs):
        query = BlogPost.objects.all().order_by('pk')
        return query

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['posts'] = self.get_queryset()
        context['tags'] = BlogTag.objects.all()
        return context

class SinglePostView(DetailView):
    model = BlogPost
    template_name = 'post.html'
    context_object_name = 'article'

    def get_queryset(self, *args, **kwargs):
        query = BlogPost.objects.filter(slug=self.kwargs['slug'])
        return query

class PostsTagView(ListView):
    model = BlogPost
    template_name = 'posts.html'
    context_object_name = 'articles'

    def get_queryset(self, *args, **kwargs):
        query = BlogPost.objects.filter(tags__slug=self.kwargs['slug'])
        return query


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

class ProfieView(UpdateView):
    form_class = CustomChangeUserForm
    template_name = 'profile.html'
    success_url = reverse_lazy('home')

    def get_queryset(self, *args, **kwargs):
        return User.objects.filter(pk=self.kwargs['pk'])

# Create your views here.
