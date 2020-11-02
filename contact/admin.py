from django.contrib import admin

# Register your models here.
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','email', 'text', 'created_time']

admin.site.register(Contact,ContactAdmin)