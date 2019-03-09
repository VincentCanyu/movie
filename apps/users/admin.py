from django.contrib import admin
from .models import Movie_detail,Category
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id','name','to_star')

admin.site.register(Movie_detail,MovieAdmin)
admin.site.register(Category)