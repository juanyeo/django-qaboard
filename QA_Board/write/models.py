from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=400)
    askedBy = models.CharField(max_length=24)
    askedDate = models.DateTimeField(auto_now=True)