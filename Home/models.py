from django.db import models

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
    
class LeftPost(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=13)
    slug = models.CharField(max_length=130)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + ' by ' + self.author
    
class RightPost(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=13)
    slug = models.CharField(max_length=130)
    timestamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + ' by ' + self.author