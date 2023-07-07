from django.db import models

# Create your models here.
class Theme(models.Model):
    directory = models.CharField(max_length=10, null=True)
    theme = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField("date published")
