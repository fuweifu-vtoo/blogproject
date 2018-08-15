from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Image ,Userip,VisitNumber



class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'href','created_time', 'author']
class UseripAdmin(admin.ModelAdmin):
    list_display = ['ip', 'count']
class VisitNumberAdmin(admin.ModelAdmin):
    list_display = ['page_name', 'count']

admin.site.register(Image,ImageAdmin)
admin.site.register(Userip,UseripAdmin)
admin.site.register(VisitNumber,VisitNumberAdmin)
