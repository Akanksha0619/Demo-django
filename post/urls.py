from django.contrib import admin
from django.urls import path
from .views import PostListView, PostDetailView, PostUpdateView, PostDeleteView
from . import views
from .views import feedback,contact_list
from .views import preparation_view, contact_form
from .views import message_list
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', PostListView.as_view(), name='home'),
    path('create_post/', views.create_post, name='create_post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('posts-by-date/<str:date>/', views.posts_by_date, name='posts-by-date'),
    path('user/<int:user_id>/', views.user_profile_and_posts, name='user-profile'),
    path('feedback/', feedback, name='feedback'),
    path('feedbacks/', views.feedback_list, name='feedback_list'),
    # path('contacts/', contact_list, name='contact_list'),
    path('preparation/', preparation_view, name='preparation'),
    path('contact/', views.contact_form, name='contact_form'),
    path('messages/', message_list, name='message_list'),
    path('password_reset/', auth_views.PasswordResetView. as_view(), name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('job_search/', views.job_search, name='job_search'),

]












