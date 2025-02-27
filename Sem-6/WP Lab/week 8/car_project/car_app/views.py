from django.shortcuts import render

def car_form(request):
    manufacturers = ["Toyota", "Ford", "Honda", "BMW", "Tesla"]
    return render(request, 'car_app/car_form.html', {'manufacturers': manufacturers})

def result(request):
    if request.method == "GET":
        manufacturer = request.GET.get('manufacturer', 'Unknown')
        model = request.GET.get('model', 'Unknown')
        return render(request, 'car_app/result.html', {'manufacturer': manufacturer, 'model': model})
