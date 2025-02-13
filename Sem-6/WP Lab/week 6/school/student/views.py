from django.shortcuts import render
from .forms import StudentForm

def student_view(request):
    form = StudentForm()
    student_data = None
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student_data = form.cleaned_data
            percentage = (student_data['english_marks'] + student_data['physics_marks'] + student_data['chemistry_marks']) / 3
            student_data['percentage'] = percentage
    return render(request, 'student_form.html', {'form': form, 'student_data': student_data})
