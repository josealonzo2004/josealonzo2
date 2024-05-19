from django.db import models
from django.db.models.fields import CharField, URLField
from cloudinary.models import CloudinaryField

# Create your models here.
class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    reseña = models.TextField(blank=True)
    image = CloudinaryField('image')
    url = URLField(blank=True)
    
    
