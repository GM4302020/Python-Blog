from django.urls import path
from .views import HomeView, SinglePostView, PostsTagView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<slug>/', SinglePostView.as_view(), name='article'),
    path('tag/<slug>/', PostsTagView.as_view(), name='tag')
]