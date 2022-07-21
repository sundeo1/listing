from django.db import models
from datetime import datetime

class Seller(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    top_seller = models.BooleanField(default=False)
    date_onboarded = models.DateTimeField(default=datetime.now, blank=True)
    date_expired = models.DateTimeField(blank=False)

    def __str__(self):
        return self.name
