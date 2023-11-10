from django.contrib import admin

from .models import Genre, Book, Ville, Gare, Voyage, Train

# Register your models here.
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Train)
admin.site.register(Voyage)
admin.site.register(Ville)
admin.site.register(Gare)
