from django.db import models

# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=256)
    user_id = models.TextField()
