from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    name = models.CharField(max_length=1000)
    subject = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    message = models.TextField()

    def __str__(self):
        return self.email