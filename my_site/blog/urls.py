from django.urls import path
from . import views

urlpatterns = [
    # A summary of the posts
    path('', views.index, name='index'),

    # An overview of all posts
    path('posts/', views.posts, name='posts'),

    # a single datailed view of a post
    path('posts/<slug:post_id>', views.post, name='post') # slug transformer checks that it only contains alphanumeric characters and dashes
]

