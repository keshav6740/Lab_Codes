from django import forms

class EmployeeForm(forms.Form):
    EMPLOYEE_CHOICES = [(str(i), f'Employee {i}') for i in range(1001, 1010)]
    employee_id = forms.ChoiceField(choices=EMPLOYEE_CHOICES)
    joining_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
