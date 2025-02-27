from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

# Home page view
def home(request):
    return render(request, 'home.html')  # Render the home page template

# Generate magazine cover view
def generate_cover(request):
    if request.method == 'POST':
        image = request.FILES['image']
        background_color = request.POST['background_color']
        font_size = request.POST['font_size']
        font_color = request.POST['font_color']
        title = request.POST['title']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)

        return render(request, 'cover_result.html', {
            'uploaded_file_url': uploaded_file_url,
            'background_color': background_color,
            'font_size': font_size,
            'font_color': font_color,
            'title': title,

        })

    # If it's a GET request, display the form
    return render(request, 'generate_cover.html')
