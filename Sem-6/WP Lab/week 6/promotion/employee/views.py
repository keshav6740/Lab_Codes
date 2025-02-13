from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee
from datetime import date

def employee_form(request):
    employees = Employee.objects.all()
    return render(request, 'employee_forms.html', {'employees': employees})

def check_promotion(request):
    if request.method == 'POST':
        emp_id = request.POST.get('emp_id')
        employee = Employee.objects.get(emp_id=emp_id)
        doj = employee.date_of_joining
        experience = (date.today() - doj).days // 365

        eligible = "YES" if experience >= 5 else "NO"
        return JsonResponse({'eligible': eligible})
