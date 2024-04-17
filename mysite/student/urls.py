from django.urls import path
from . import views

urlpatterns = [
    path('homescreen/', views.home_screen, name='homescreen')
]