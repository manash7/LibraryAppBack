from django.contrib import admin
<<<<<<< HEAD
from .models import customusers,Books

# Register your models here.

@admin.register(customusers)
class userAdmin(admin.ModelAdmin):
    list_display = ['id']    

@admin.register(Books)
class booksAdmin(admin.ModelAdmin):
    list_display = ['id','title','price']
=======

# Register your models here.
>>>>>>> 0ac8604088d6005171f4615d8222636f4885af6c
