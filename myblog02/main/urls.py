from django.urls import path
from .views import HomeView, SinglePostView, PostsTagView, SignUpView, ProfieView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<slug>/', SinglePostView.as_view(), name='article'),
    path('tag/<slug>/', PostsTagView.as_view(), name='tag'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('prfile/<pk>/', ProfieView.as_view(),name='profile')
]