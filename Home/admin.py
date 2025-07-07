from django.contrib import admin
from Home.models import Contact
from Home.models import LeftPost
from Home.models import RightPost
# Register your models here.

admin.site.register(Contact)
admin.site.register(LeftPost)
admin.site.register(RightPost)