from django.db import models

# Create your models here.

class Mention(models.Model):
    title = models.TextField()
    content = models.TextField()
    writer = models.TextField()