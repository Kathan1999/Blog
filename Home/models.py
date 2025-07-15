from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    name = models.CharField(max_length=1000)
    subject = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.email
    

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=14)
    slug = models.CharField(max_length=130)
    timestamp = models.DateTimeField(blank=True)
    content = models.TextField()

    def __str__(self):
        return self.title + " by " + self.author
    

class BlogComment(models.Model):
    sno = models.AutoField(primary_key = True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

