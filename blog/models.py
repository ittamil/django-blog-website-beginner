from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related

# Create your models here.
class Blogpost(models.Model):
    title = models.CharField(max_length=100,blank=True,null=True)
    content = models.TextField(max_length=5000,blank=True,null=True)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    thumbnail = models.ImageField(upload_to="thumbnail/")
    author = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Blogpost, on_delete=models.CASCADE,related_name="comments",null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    content = models.TextField(max_length=5000,blank=True,null=True)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name
    
class Video(models.Model):
    video = models.FileField(max_length=10000,upload_to="video/")