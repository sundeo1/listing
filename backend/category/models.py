from django.db import models
from datetime import datetime

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    

    def __str__(self):
        return self.name
