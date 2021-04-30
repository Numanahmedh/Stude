from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.events_view, name='events_view'),


]
