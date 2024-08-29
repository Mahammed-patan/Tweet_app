from django.db import models

# Create your models here.

class Tweet(models.Model):
    text = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=[
        ('fresher', 'Fresher'),
        ('experienced', 'experienced'),
        ])
