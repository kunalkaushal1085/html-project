from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register_user'),
    path('login/', views.user_login, name='user_login'),
    path('create_post/', views.create_post, name='create_post'),
    path('posts/', views.get_all_posts, name='get_all_posts'),
]
