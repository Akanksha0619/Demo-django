from django.contrib import admin
from django.urls import path
from .views import PostListView, PostDetailView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('create_post/', views.create_post, name='create_post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('posts-by-date/<str:date>/', views.posts_by_date, name='posts-by-date'),
    path('user/<int:user_id>/', views.user_profile_and_posts, name='user-profile'),
    path('about/', views.about, name='about'),

]