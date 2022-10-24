from django.urls import path
from .views import (HomeView,
                    SinglePostView,
                    PostsTagView,
                    SignUpView,
                    ProfieView,
                    ReviewOnPost,
                    DeleteReview
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<slug>/', SinglePostView.as_view(), name='article'),
    path('tag/<slug>/', PostsTagView.as_view(), name='tag'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<pk>/', ProfieView.as_view(), name='profile'),
    path('reviewonpost/', ReviewOnPost.as_view(), name='reviewonpost'),
    path('deletereview/<pk>/', DeleteReview.as_view(), name='deletereview')

]