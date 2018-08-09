from django.contrib import admin

# Register your models here.
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'text', 'created_time', 'post']

admin.site.register(Comment,CommentAdmin)