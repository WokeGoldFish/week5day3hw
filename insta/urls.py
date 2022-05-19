from cgitb import html
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name= 'home'),
    path('about/', views.about, name='about'),
    path('posts/create/', views.createPost, name='createpost'),
    path('posts/<int:post_id>', views.singlePost, name='post'),
    path('posts/update/<int:post_id>', views.updatePost, name='update-post'),
    
    
    path('posts/update/<int:post_id>', views.updatePost, name='delete-post')
]