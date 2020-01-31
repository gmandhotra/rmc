from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ImageDeatil(models.Model):
     type_image = (('t1', 'Type 1'), ('t2', 'Type 2'))
     image_id = models.CharField(unique=True, max_length=20)
     image_name = models.ImageField(upload_to='uploaded/')
     image_type = models.CharField(max_length=3, choices=type_image)
     cm_length = models.CharField(max_length=100, )
     x1_y1_length = models.CharField(max_length=100)
     x2_y2_length = models.CharField(max_length=100)
     material_information = models.CharField(max_length=100)



class Upload(models.Model):


     user = models.ForeignKey(User, on_delete=models.CASCADE)
     image_detail = models.ForeignKey(ImageDeatil, on_delete=models.CASCADE)
     latitude = models.DecimalField(max_digits=9, decimal_places=6)
     longitude = models.DecimalField(max_digits=9, decimal_places=6)
     available_qty = models.CharField(max_length=100,)
     available_till = models.DateField()
     available_now = models.BooleanField(default=True)
     uploaded_date = models.DateField(auto_now_add=True)


