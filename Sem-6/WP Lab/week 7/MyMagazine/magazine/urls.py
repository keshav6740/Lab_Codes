from django.urls import path
from . import views

urlpatterns = [
    path('generate_cover/', views.generate_cover, name='generate_cover'),  # Add this line for the generate_cover view
]
