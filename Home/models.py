from django.db import models

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('pubmished', 'Published'),
    )

    title = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    featured_image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    author = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='products')
    product_name = models.CharField(max_length=255)
    product_image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    affiliate_link = models.URLField()
    price = models.CharField(max_length=50, blank=True)
    rating = models.FloatField(default=0)
    pros = models.TextField(blank=True)
    cons = models.TextField(blank=True)
    button_text = models.CharField(max_length=50, default='Buy Now')
    position = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name