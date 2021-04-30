from django.urls import path
from . import views

urlpatterns = [
    path('request_notes/', views.request_notes, name='request_notes'),
    path('upload_notes/', views.upload_notes, name='upload_notes'),
    path('available_notes/', views.available_notes, name='available_notes'),


]
