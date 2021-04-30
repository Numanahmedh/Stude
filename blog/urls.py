from django.urls import path, include
from . import views

urlpatterns = [
    path('blogs/', views.blog, name='blogs'),
    path('create_blog/', views.create_blog, name='create_blog'),
    path('blog_view/', views.blog_view, name='blog_view'),
]
