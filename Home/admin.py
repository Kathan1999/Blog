from django.contrib import admin
from Home.models import Contact
from Home.models import Post
from Home.models import BlogComment
# Register your models here.

admin.site.register(Contact)
admin.site.register(Post)
admin.site.register(BlogComment)

