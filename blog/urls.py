from django.urls import path
from . import views


app_name = "blog"

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/category/<int:id>', views.posts_by_category, name='posts_by_category'),
    path('post/tag/<int:id>/', views.posts_by_tag, name='posts_by_tag'),
    path('post/author/<int:id>/', views.posts_by_author, name='posts_by_author'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<str:slug>/', views.post_detail, name='post_detail'),
    path('post-edit/<str:slug>/', views.post_edit, name='post_edit'), 
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('profile_edit/',views.profile_edit, name='profile_edit'),
    path('posts/', views.post_list, name='post_list'),
    ]