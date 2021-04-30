from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.loginview, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
]
