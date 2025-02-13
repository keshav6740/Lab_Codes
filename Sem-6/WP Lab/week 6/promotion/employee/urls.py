from django.urls import path
from .views import employee_form, check_promotion

urlpatterns = [
    path('', employee_form, name='employee_form'),
    path('check_promotion/', check_promotion, name='check_promotion'),
]
