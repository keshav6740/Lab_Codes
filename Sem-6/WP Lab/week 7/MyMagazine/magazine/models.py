# models.py

from django.db import models

class MagazineCover(models.Model):
    image = models.ImageField(upload_to='covers/')  # Ensure that images are saved in 'media/covers/'
    background_color = models.CharField(max_length=7)  # Store color code like '#FFFFFF'
    font_color = models.CharField(max_length=7)
    font_size = models.IntegerField()
    font_family = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
