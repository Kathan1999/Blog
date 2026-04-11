from django.contrib import admin
from Home.models import Post
from Home.models import Product
from Home.models import Category
# Register your models here.

class ProductInline(admin.TabularInline):
    model = Product
    extra = 1
    
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

    inlines = [ProductInline]



admin.site.register(Post, PostAdmin)
admin.site.register(Product)
admin.site.register(Category)