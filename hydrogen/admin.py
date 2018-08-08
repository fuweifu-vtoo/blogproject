from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Image



class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'href','created_time', 'author']

admin.site.register(Image,ImageAdmin)
