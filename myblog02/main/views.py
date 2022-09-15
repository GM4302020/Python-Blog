from django.views.generic import ListView
from .models import BlogTag, BlogPost

class HomeView(ListView):
    #model = BlogTag
    template_name= 'index.html'
    #context_object_name = 'tags'

    def get_queryset(self, *args, **kwargs):
        query = BlogPost.objects.all().order_by('-pk')
        return query

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['posts'] = self.get_queryset()
        context['tags'] = BlogTag.objects.all()
        return context

# Create your views here.
