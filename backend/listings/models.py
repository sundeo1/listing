from django.db import models
from django.utils.timezone import now
from seller.models import Seller

class Listing(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
    slug = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_9 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_10 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_11 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_12 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_13 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_14 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_15 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_16 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_17 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_18 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_19 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_20 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.title