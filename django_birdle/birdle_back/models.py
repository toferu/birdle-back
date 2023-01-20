from django.db import models

# Create your models here.
class Bird(models.Model):
    name = models.CharField(max_length=8)
    image = models.URLField(max_length=350)

    