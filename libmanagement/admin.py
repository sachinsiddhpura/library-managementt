from django.contrib import admin

# Register your models here.
from .models import Book,Issue,Log

admin.site.register(Book)
admin.site.register(Log)
admin.site.register(Issue)