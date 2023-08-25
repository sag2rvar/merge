# Api/urls.py
from django.urls import path
from .Views.auth import LoginView, SignupView ,UserProfileView, ProfileEditView
from .Views.blog import UserPostsView, UserPostscreate,UserPostedit, PostDeleteView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('profile/edit/', ProfileEditView.as_view(), name='user-profile-edit'),
    path('user/posts/', UserPostsView.as_view(), name='user-posts'),
    path('posts_create/', UserPostscreate.as_view(), name='posts_create'),
    path('posts_edit/', UserPostedit.as_view(), name='posts_edit'),
    path('posts_Delete/<int:id>/', PostDeleteView.as_view(), name='posts_Delete'),

]