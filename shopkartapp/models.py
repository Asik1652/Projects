from django.db import models
import datetime
import os

# Create your models here.

def getFileName(request, fileName):
    current_time = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    newFileName = '%s%s'%(fileName, current_time)
    STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads', newFileName)

    return STATIC_DIR

class Category(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=getFileName, null=True, blank=True)
    description = models.TextField(max_length=500,null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0-show,1-Hidden")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=False, blank=False)
    vendor = models.CharField(max_length=150, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    prod_image = models.ImageField(upload_to=getFileName, null=True, blank=True)
    description = models.TextField(max_length=500,null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0-show,1-Hidden")
    trend = models.BooleanField(default=False, help_text="0-default,1-Trending")
    created_at = models.DateTimeField(auto_now_add=True)
