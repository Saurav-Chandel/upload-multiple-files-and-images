from django.db import models
import django
# # Create your models here.


# class Blogs(models.Model):
#     name=models.CharField(max_length=100,blank=True,null=True)
#     created_at=models.DateTimeField(default=django.utils.timezone.now)


# class Photo(models.Model):
#     # blogs = models.ForeignKey(Blogs,on_delete=models.CASCADE, related_name='blogs_img')
#     image = models.ImageField(upload_to='images')







#Another pproach 

class Product(models.Model):
   title = models.CharField(max_length=255)
   description = models.CharField(max_length=255)

class Images(models.Model):
   product = models.ForeignKey('Product', related_name="images", on_delete=models.CASCADE)
   image = models.ImageField(upload_to='2nd_approach')