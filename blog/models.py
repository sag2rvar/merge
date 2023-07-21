from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser 
from autoslug import AutoSlugField

class User(AbstractUser):
    email = models.EmailField(unique = True)
    phone_no = models.CharField(max_length = 10)
    image = models.ImageField(upload_to='user_images/') 
    gender = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=50,default='')
    city = models.CharField(max_length=50,default='')

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=100)
    # Add any additional fields you need for the category

    def __str__(self):  
        return self.name    

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)  
    tags = models.ManyToManyField(Tag)
    featured_image = models.ImageField(upload_to='featured_images/', blank=True, null=True)
    thumbnail_image = models.ImageField(upload_to='thumbnail_images/', blank=True, null=True)
    slug = AutoSlugField(populate_from='title' , unique=True)
      

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    text = models.TextField(max_length=200)
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    parent = models.ForeignKey('self' , null=True , blank=True , on_delete=models.CASCADE , related_name='replies')
    
    
    def __str__(self):
        return str(self.name) + ' comment ' + str(self.text)

    @property
    def children(self):
        return Comment.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False


